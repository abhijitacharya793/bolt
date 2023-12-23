from colorama import Fore

from src.main.cli.auxiliary.decorators.dWorkflow import workflow


@workflow(name="ssti", type="fuzzing", severity="critical", confidence="confirmed")
def execute(scan_type, mode, target, config, scan_id):
    print(f'{Fore.GREEN}[INFO]{Fore.YELLOW} Ssti_fuzz')

    return "", "", ""
