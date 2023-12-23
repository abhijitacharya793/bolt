from colorama import Fore

from src.main.cli.auxiliary.decorators.dWorkflow import workflow
from src.main.cli.auxiliary.utils.fileSystem import create_valid_path

from src.test.cli.tools.burp_json.core.tool import Burp_json
from src.test.cli.tools.create_template.core.tool import Create_template
from src.test.cli.tools.login.core.tool import Login
from src.test.cli.tools.nuclei.core.tool import Nuclei
from src.test.cli.tools.request_replace.core.tool import RequestReplace

from src.config import PWD


@workflow(name="xss", type="fuzzing", severity="high", confidence="not_confirmed")
def execute(scan_type, mode, target, config, scan_id):
    print(f'{Fore.GREEN}[INFO]{Fore.YELLOW} XSS fuzz')

    # LOGIN
    if config['login']:
        cookie = Login() \
            .json_file(config['login']) \
            .execute().results[0]
    else:
        cookie = ""

    # CREATE REQUESTS JSON
    Burp_json() \
        .input(config['burp_export']) \
        .output(create_valid_path(config['execution_dir'], "burp_export.json")) \
        .execute()

    # REPLACE {{injection}} IN JSON REQUEST
    rr = RequestReplace() \
        .input(create_valid_path(config['execution_dir'], "burp_export.json")) \
        .working_dir(config['execution_dir']) \
        .inject("\"{{injection}}\"") \
        .part("query,header,body") \
        .execute().results[0]

    # REPLACE {{url_encode(injection)}} IN JSON REQUEST AND APPEND
    rr = RequestReplace() \
        .input(create_valid_path(config['execution_dir'], "burp_export.json")) \
        .working_dir(config['execution_dir']) \
        .inject("\"{{url_encode(injection)}}\"") \
        .part("query,header,body") \
        .append() \
        .execute().results[0]

    # CREATE NUCLEI TEMPLATE
    ct = Create_template() \
        .template(PWD + "/src/test/resources/templates/nuclei/fuzzing/xss_fuzz.yaml") \
        .working_dir(config['execution_dir']) \
        .output("xss_fuzz") \
        .requests(rr) \
        .execute().results[0]

    # RUN SCAN
    nuclei = Nuclei() \
        .target(target) \
        .templates(ct.replace("\n", "")) \
        .include_rr() \
        .header("Cookie:" + cookie.replace("\n", "")) \
        .markdown_export(create_valid_path(config['execution_dir'], "result_xss_fuzz")) \
        .rate_limit(config['rate_limit']) \
        .execute()

    return nuclei.results
