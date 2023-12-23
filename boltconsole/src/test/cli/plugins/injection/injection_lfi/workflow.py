from colorama import Fore

from src.main.cli.auxiliary.decorators.dWorkflow import workflow


@workflow(name="lfi", type="injection", severity="critical", confidence="not_confirmed")
def execute(scan_type, mode, target, config, scan_id):
    print(f'{Fore.GREEN}[INFO]{Fore.YELLOW} Injection_lfi')

    # CALL TOOLS
    return "", "", ""