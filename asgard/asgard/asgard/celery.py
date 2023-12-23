import json
import os, requests
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asgard.settings')

app = Celery("asgard")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'get_scan': {
        'task': 'asgard.celery.trigger_scan',
        'schedule': 30.0
    }
}


def get_all_scans():
    return json.loads(requests.get("http://midgard-api:8335/midgard/v1/enricher?triggered=False").text)


def get_vulnerability(vulnerability_id):
    return json.loads(requests.get(
        f"http://yggdrasil-api:8337/yggdrasil/v1/risk/vulnerability?vulnerability_id={vulnerability_id}").text)


def get_workflow(vulnerability_id, workflow_id, root):
    return json.loads(requests.get(
        f"http://yggdrasil-api:8337/yggdrasil/v1/risk/workflow?root={root}&vulnerability_id={vulnerability_id}&workflow_id={workflow_id}").text)


def get_script(script_id):
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


@app.task
def trigger_scan():
    print("Get scans from midgard and run")

    # TODO: Call midgard and get queued api scans
    scans = get_all_scans()

    # TODO: pick an api and for each vulnerability recommended by midgard
    #     get script from yggdrasil for the vulnerability and level
    #     trigger a scan in docker
    for scan in scans:
        for vulnerability_id in scan['scans'].split(","):
            # vulnerability = get_vulnerability(vulnerability_id)
            workflow_tree = get_workflow_tree(vulnerability_id)
            for workflow in workflow_tree:
                run_workflow(workflow)
        break

    # TODO: get output of each scan and send it to hiemdall (hiemdall will update it to bifrost)
    return


app.autodiscover_tasks()
