import json
import os, requests
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


# GET QUEUED TASKS
def get_all_queued_tasks():
    return json.loads(requests.get("http://valhalla-api:8335/valhalla/v1/enricher?triggered=False").text)


# MARK TASK TRIGGERED
def mark_task_triggered(task):
    task['triggered'] = True
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
        # ADD QUERY PARAM
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
def add_result():
    pass


# RUN COMMAND
def run_command(api, vulnerability):
    # save request to file
    with open("request.api", 'w') as req_file:
        req_file.write(api.__str__())
    os.popen(f"{_CP}/asgard/request.api ragnarok:/ragnarok/request.api")
    # TODO: create nuclei template
    templates = get_template(vulnerability)

    for template in templates:
        os.popen(f"{_EXEC}ragnarok python3 /yggdrasil/resources/utils/create_template.py --template {template['path']}")
    # TODO: create payloads
    # get command
    command = get_vulnerability(vulnerability)['command']
    command = command.replace("{{TARGET}}",api.target)
    # run script on ragnarok
    output_str = os.popen(f'{_EXEC}ragnarok {command}').read()
    # parse output
    if output_str!=None and output_str!='':
        output = json.loads(output_str)
        print("####################################################")
        print(output['template-id'])
        print(output['host'])
        print(output['url'])
        print(output['matched-at'])
        print(output['meta']['payloadStr'])
        print(output['curl-command'])
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        # TODO: get output of each task and send it to hiemdall (hiemdall will update it to bifrost)
        a=1
    else:
        print("####################################################")
        print("NO FINDINGS!!!")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    
    

    # clean up and copy request to ragnarok
    os.popen(f"{_EXEC}ragnarok rm -rf /ragnarok/input/").read()
    os.popen(f"{_EXEC}ragnarok rm -rf /ragnarok/export/").read()
    os.popen(f"{_EXEC}ragnarok mkdir /ragnarok/input").read()
    os.popen(f"{_EXEC}ragnarok mkdir /ragnarok/export").read()


@app.task
def trigger_task():
    # get tasks from valhalla
    tasks = get_all_queued_tasks()

    # pick an api and for each vulnerability recommended by valhalla
    #     get script from yggdrasil for the vulnerability and level
    #     trigger a task in docker
    for task in tasks:
        api = get_api_details(task['uuid'])
        if task['tasks']:
            # for each task corresponding to an API
            for vulnerability_id in task['tasks'].split(","):
                run_command(api, vulnerability_id)
            mark_task_triggered(task)
        # break out of the loop
        break

    return


app.autodiscover_tasks()
