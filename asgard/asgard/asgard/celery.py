import json
import os, requests
import subprocess
from random import randrange
from celery import Celery

# constants
_EXEC = "docker exec "
_CP = "docker cp "

# CELERY
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asgard.settings')

app = Celery("asgard")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'get_task': {
        'task': 'asgard.celery.trigger_task',
        'schedule': 30.0
    }
}


# GET TASKS BY STATUS
def get_tasks_status(status):
    return json.loads(requests.get(f"http://valhalla-api:8335/valhalla/v1/enricher?status={status}").text)

# UPDATE TASK STATUS
def update_task_status(task, status):
    task['status'] = status
    return json.loads(requests.put(f"http://valhalla-api:8335/valhalla/v1/enricher/{task['id']}/", data=task).text)

# UPDATE TASK COMPLETION
def update_task_completion(task, completion):
    task['completion'] = completion
    return json.loads(requests.put(f"http://valhalla-api:8335/valhalla/v1/enricher/{task['id']}/", data=task).text)


# API OBJECT
class API:
    def __init__(self, uuid, target, root_domain, domain, protocol, protocol_version, port, method, path, body,
                 header_object, query_object):
        self.uuid = uuid
        self.target = target
        self.root_domain = root_domain
        self.domain = domain
        self.protocol = protocol
        self.protocol_version = protocol_version
        self.port = port
        self.method = method
        self.path = path
        self.body = body
        self.header_object = header_object
        self.query_object = query_object

    def __str__(self):
        api_string = f"{self.method} {self.path}?"
        # TODO: ADD QUERY PARAM
        # print(self.query_object)
        for query_param in self.query_object:
            api_string += f"{query_param['name']}={query_param['value']}&"
        api_string += f" {self.protocol_version}\n"
        for header in self.header_object:
            api_string += f"{header['name']}: {header['value']}\n"
        return api_string


def get_api_details(uuid):
    header = json.loads(requests.get(f"http://bifrost-api:8333/bifrost/v1/api/header/?uuid={uuid}").text)
    query_param = json.loads(requests.get(f"http://bifrost-api:8333/bifrost/v1/api/query/?uuid={uuid}").text)
    api = json.loads(requests.get(f"http://bifrost-api:8333/bifrost/v1/api/?uuid={uuid}").text)[0]
    api = API(api['uuid'], api['target'], api['root_domain'], api['domain'], api['protocol'], api['protocol_version'],
              api['port'], api['method'], api['path'], api['body'], header, query_param)
    return api


def get_vulnerability(vulnerability_id):
    return json.loads(requests.get(
        f"http://yggdrasil-api:8337/yggdrasil/v1/risk/vulnerability/{vulnerability_id}").text)


def get_template(vulnerability_id):
    return json.loads(requests.get(
        f"http://yggdrasil-api:8337/yggdrasil/v1/risk/template/?vulnerability_id={vulnerability_id}").text)


# ADD RESULT TO HIEMDALL
def add_result(scan_id, uuid, template_id, payloadStr, matched_at, curl_command, vulnerability):
    data = {"scan_id":scan_id, "uuid":uuid, "template_id":template_id, "payload_str":payloadStr, "matched_at":matched_at, "curl_command":curl_command, "vulnerability_id":vulnerability}
    return json.loads(requests.post(f"http://hiemdall-api:8338/hiemdall/v1/result/", data=data).text)

# RUN COMMAND
def run_command(api, vulnerability, scan_id):
    # get command
    command = get_vulnerability(vulnerability)['command']
    if command==None or command=='':
        print("####################################################")
        print("NO COMMAND CONFIGURED!!!")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return
    command = command.replace("{{TARGET}}",api.domain)
    
    # save request to file
    with open("request.api", 'w') as req_file:
        req_file.write(api.__str__())
    subprocess_output, subprocess_error = subprocess.Popen(f"{_CP}/asgard/request.api ragnarok:/ragnarok/request.api", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    templates = get_template(vulnerability)

    for template in templates:
        subprocess_output, subprocess_error = subprocess.Popen(f"{_EXEC}ragnarok python3 /yggdrasil/resources/utils/create_template.py --template {template['path']}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    
    template_count, subprocess_error = subprocess.Popen(f"{_EXEC}ragnarok ls /ragnarok/input/ | wc -w", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    print("####################################################")
    print(f"TEMPLATES CREATED => {template_count.decode()}")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    # TODO: create payloads
    # run script on ragnarok
    subprocess_output, subprocess_error = subprocess.Popen(f"{_EXEC}ragnarok {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    output_str = subprocess_output.decode()
    # parse output
    if output_str!=None and output_str!='':
        # TODO: GET BETTER APPROACH
        output_str_split = output_str.replace("}\n{", "}<#$>{").split("<#$>")
        for output in output_str_split:
            output = json.loads(output)
            print("####################################################")
            print(output['template-id'])
            print(output['host'])
            print(output['url'])
            print(output['matched-at'])
            print(output['meta']['payloadStr'])
            print(output['curl-command'])
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            # TODO: get output of each task and send it to hiemdall (hiemdall will update it to bifrost)
            print(add_result(scan_id, api.uuid, output['template-id'], output['meta']['payloadStr'], output['matched-at'], output['curl-command'], vulnerability))
    else:
        print("####################################################")
        print("NO FINDINGS!!!")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    
    # clean up and copy request to ragnarok
    template_count, subprocess_error = subprocess.Popen(f"{_EXEC}ragnarok ls /ragnarok/input/ | wc -w", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    subprocess_output, subprocess_error = subprocess.Popen(f"{_EXEC}ragnarok rm -rf /ragnarok/input/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    subprocess_output, subprocess_error = subprocess.Popen(f"{_EXEC}ragnarok rm -rf /ragnarok/export/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    subprocess_output, subprocess_error = subprocess.Popen(f"{_EXEC}ragnarok mkdir /ragnarok/input", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    subprocess_output, subprocess_error = subprocess.Popen(f"{_EXEC}ragnarok mkdir /ragnarok/export", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    print("####################################################")
    print(f"TEMPLATES CLEANED UP => {template_count.decode()}")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


@app.task
def trigger_task():
    # get tasks from valhalla
    running_tasks = get_tasks_status(2)
    if len(running_tasks)>0:
        print("####################################################")
        print("TASK ALREADY RUNNING!!!")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return
    created_tasks = get_tasks_status(1)

    # pick an api and for each vulnerability recommended by valhalla
    #     get script from yggdrasil for the vulnerability and level
    #     trigger a task in docker
    for task in created_tasks:
        api = get_api_details(task['uuid'])
        if task['tasks']:
            task_count = 0
            task_length = len(task['tasks'].split(","))
            # for each task corresponding to an API
            for vulnerability_id in task['tasks'].split(","):
                update_task_status(task, 2)
                run_command(api, vulnerability_id, task['scan_id'])
                # TODO: UPDATE TASK COMPLETION
                task_count+=1
                update_task_completion(task, int((task_count*100)/task_length))
            update_task_status(task, 3)
        # break out of the loop
        break
    return

app.autodiscover_tasks()
