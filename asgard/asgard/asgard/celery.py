import json
import os, requests
from celery import Celery

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


def get_workflow(vulnerability_id, workflow_id, root):
    return json.loads(requests.get(
        f"http://yggdrasil-api:8337/yggdrasil/v1/risk/workflow?root={root}&vulnerability_id={vulnerability_id}&workflow_id={workflow_id}").text)


def get_script(script_id):
    script_name = json.loads(requests.get(
        f"http://yggdrasil-api:8337/yggdrasil/v1/risk/script?script_id={script_id}").text)[0]["script"].split("/")[-1]
    return script_name


def get_workflow_tree(vulnerability_id):
    root = get_workflow(vulnerability_id, "", "True")
    if len(root) < 1:
        print("IMPLEMENT THE WORKFLOW!!!")
        return []
    wfs = [root[0]]
    cont = True
    while len(wfs) > 0 and cont:
        workflow = get_workflow(vulnerability_id, wfs[-1]['id'], "False")
        if len(workflow) > 0:
            wfs.append(workflow[0])
        else:
            cont = False
    return wfs


def run_workflow(api, workflow, previous_output):
    print(workflow)
    # GET SCRIPT TO RUN
    script_name = get_script(workflow['script'])
    with open("request.api", 'w') as req_file:
        req_file.write(api.__str__())
    with open("output.api", 'w') as out_file:
        out_file.write(previous_output)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ RUN SCRIPT $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    # copy request and previous output to ragnarok
    os.popen(f"docker cp /asgard/request.api ragnarok:/ragnarok/request.api")
    os.popen(f"docker cp /asgard/output.api ragnarok:/ragnarok/output.api")
    # run script on ragnarok
    return os.popen(
        f'docker exec ragnarok python3 /yggdrasil/scripts/{script_name} --api request.api --target {api.target} --domain {api.domain} --previous_output output.api').read()


@app.task
def trigger_task():
    # get tasks from valhalla and run
    tasks = get_all_queued_tasks()

    # pick an api and for each vulnerability recommended by valhalla
    #     get script from yggdrasil for the vulnerability and level
    #     trigger a task in docker
    for task in tasks:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ TASK DETAILS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        api = get_api_details(task['uuid'])

        if task['tasks']:
            # for each task corresponding to an API
            for vulnerability_id in task['tasks'].split(","):
                workflow_tree = get_workflow_tree(vulnerability_id)
                previous_output = None
                for workflow in workflow_tree:
                    previous_output = run_workflow(api, workflow, previous_output)
                    # TODO: get output of each task and send it to hiemdall (hiemdall will update it to bifrost)
                    print(previous_output)
        # break out of the loop
        break

    return


app.autodiscover_tasks()
