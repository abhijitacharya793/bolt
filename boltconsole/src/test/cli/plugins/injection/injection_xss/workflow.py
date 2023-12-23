import os

from colorama import Fore

from src.main.cli.auxiliary.decorators.dWorkflow import workflow
from src.main.cli.auxiliary.enums.eMode import Mode
from src.main.cli.auxiliary.utils.fileSystem import create_valid_path
from src.test.cli.tools.burp_json.core.tool import Burp_json
from src.test.cli.tools.dalfox.core.tool import Dalfox
from src.test.cli.tools.login.core.tool import Login
from src.test.cli.tools.request_replace.core.tool import RequestReplace


@workflow(name="xss", type="injection", severity="critical", confidence="not_confirmed")
def execute(scan_type, mode, target, config, scan_id):
    print(f'{Fore.GREEN}[INFO]{Fore.YELLOW} Injection_xss')
    # LOGIN
    if config['login']:
        cookie = Login() \
            .json_file(config['login']) \
            .execute().results[0]
    else:
        cookie = ""

    Burp_json() \
        .input(config['burp_export']) \
        .output(create_valid_path(config['execution_dir'], "burp_export.json")) \
        .execute()

    # REPLACE {{url_encode(injection)}} IN JSON REQUEST
    rr = RequestReplace() \
        .input(create_valid_path(config['execution_dir'], "burp_export.json")) \
        .working_dir(config['execution_dir']) \
        .inject("\"SKIP_INJECTION\"") \
        .part("query,header,body") \
        .execute().results[0]

    dalfox_results = ["dalfox", [], ""]
    for request_file in os.listdir(rr.strip()):
        dalfox = Dalfox() \
            .mode("file") \
            .request_file(rr.strip() + request_file) \
            .http("--http" if target.split("://")[0] == "http" else "") \
            .cookie("\"" + cookie.replace("\n", "") + "\"") \
            .silent() \
            .no_color() \
            .execute()
        # print(f"{Fore.GREEN}[RESULT]{Fore.YELLOW} {sqlmap.results[0]}")
        dalfox_results[1].append(dalfox.results)
    # CALL TOOLS
    return dalfox_results
