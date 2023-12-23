import os

from colorama import Fore

from src.main.cli.auxiliary.decorators.dWorkflow import workflow
from src.main.cli.auxiliary.enums.eMode import Mode
from src.main.cli.auxiliary.utils.fileSystem import create_valid_path
from src.test.cli.tools.burp_json.core.tool import Burp_json
from src.test.cli.tools.login.core.tool import Login
from src.test.cli.tools.request_replace.core.tool import RequestReplace
from src.test.cli.tools.sqlmap.core.tool import Sqlmap


@workflow(name="sqli", type="injection", severity="critical", confidence="not_confirmed")
def execute(scan_type, mode, target, config, scan_id):
    print(f'{Fore.GREEN}[INFO]{Fore.YELLOW} Injection_sqli')

    # LOGIN
    if config['login']:
        cookie = Login() \
            .json_file(config['login']) \
            .execute().results[0]
    else:
        cookie = ""

    with open(create_valid_path(config['execution_dir'], "cookie_file"), 'w') as cookie_file:
        cookie_file.write("Cookie: " + cookie)

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

    sqlmap_results = ["sqlmap", [], ""]
    for request_file in os.listdir(rr.strip()):
        sqlmap = Sqlmap() \
            .request_file(rr.strip() + request_file) \
            .level("5" if mode == Mode.aggressive else "1") \
            .risk("3" if mode == Mode.aggressive else "1") \
            .batch() \
            .skip_waf() \
            .live_cookies(create_valid_path(config['execution_dir'], "cookie_file")) \
            .delay("0.5") \
            .verbose("0") \
            .execute()
        # print(f"{Fore.GREEN}[RESULT]{Fore.YELLOW} {sqlmap.results[0]}")
        sqlmap_results[1].append(sqlmap.results)
    # CALL TOOLS
    return sqlmap_results
