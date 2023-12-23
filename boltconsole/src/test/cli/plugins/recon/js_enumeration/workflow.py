from colorama import Fore

from src.main.cli.auxiliary.decorators.dWorkflow import workflow


@workflow(name="plugin_name", type="recon", severity="critical", confidence="not_confirmed")
def execute(scan_type, mode, target, config, scan_id):
    print(f'{Fore.GREEN}[INFO]{Fore.YELLOW} Js_enumeration')


    return "", "", ""

