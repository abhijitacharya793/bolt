import json
import os, requests
from celery import Celery

# CELERY
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asgard.settings')

app = Celery("asgard")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'get_scan': {
        'task': 'asgard.celery.trigger_scan',
        'schedule': 30.0
    }
}


# API OBJECT
class API:
    def __init__(self, uuid, target, root_domain, domain, protocol, port, method, path, body, header_object,
                 query_object):
        self.uuid = uuid
        self.target = target
        self.root_domain = root_domain
        self.domain = domain
        self.protocol = protocol
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
        api_string += " HTTP/1.1\n"
        for header in self.header_object:
            api_string += f"{header['name']}: {header['value']}\n"

        return api_string


# TASK
def get_all_queued_scans():
    return json.loads(requests.get("http://valhalla-api:8335/valhalla/v1/enricher?triggered=False").text)


def get_api_details(uuid):
    header = json.loads(requests.get(f"http://bifrost-api:8333/bifrost/v1/api/header/?uuid={uuid}").text)
    query_param = json.loads(requests.get(f"http://bifrost-api:8333/bifrost/v1/api/query/?uuid={uuid}").text)
    api = json.loads(requests.get(f"http://bifrost-api:8333/bifrost/v1/api/?uuid={uuid}").text)[0]
    api = API(api['uuid'], api['target'], api['root_domain'], api['domain'], api['protocol'], api['port'],
              api['method'], api['path'], api['body'], header, query_param)
    return api


def get_vulnerability(vulnerability_id):
    return json.loads(requests.get(
        f"http://yggdrasil-api:8337/yggdrasil/v1/risk/vulnerability?vulnerability_id={vulnerability_id}").text)


def get_workflow(vulnerability_id, workflow_id, root):
    return json.loads(requests.get(
        f"http://yggdrasil-api:8337/yggdrasil/v1/risk/workflow?root={root}&vulnerability_id={vulnerability_id}&workflow_id={workflow_id}").text)


def get_script(script_id):
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    output = os.popen("whoami").read()
    print(output)
    output = os.popen("docker ps").read()
    print(output)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    return json.loads(requests.get(
        f"http://yggdrasil-api:8337/yggdrasil/v1/risk/script?script_id={script_id}").text)


def get_script_file(script_url):
    return requests.get(script_url).text


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


def run_workflow(workflow):
    print(workflow)
    # GET SCRIPT TO RUN
    script = get_script(workflow['script'])[0]
    script_file = get_script_file(script['script'])
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ RUN SCRIPT $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(script_file)


@app.task
def trigger_scan():
    print("Get scans from valhalla and run")

    scans = get_all_queued_scans()

    # TODO: pick an api and for each vulnerability recommended by valhalla
    #     get script from yggdrasil for the vulnerability and level
    #     trigger a scan in docker
    for scan in scans:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ SCAN DETAILS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(scan)
        print(get_api_details(scan['uuid']))
        if scan['scans']:
            for vulnerability_id in scan['scans'].split(","):
                # vulnerability = get_vulnerability(vulnerability_id)
                workflow_tree = get_workflow_tree(vulnerability_id)
                for workflow in workflow_tree:
                    run_workflow(workflow)
        # break out of the loop
        break

    # TODO: get output of each scan and send it to hiemdall (hiemdall will update it to bifrost)
    return


app.autodiscover_tasks()
