from colorama import Fore

from src.main.cli.auxiliary.decorators.dWorkflow import workflow
from src.test.cli.tools.login.core.tool import Login


@workflow(name="directory_bruteforce", type="recon", severity="critical", confidence="not_confirmed")
def execute(scan_type, mode, target, config, scan_id):
    print(f'{Fore.GREEN}[INFO]{Fore.YELLOW} Directory_bruteforce')

    # LOGIN
    if config['login']:
        cookie = Login() \
            .json_file(config['login']) \
            .execute().results[0]
    else:
        cookie = ""

    return "", "", ""
