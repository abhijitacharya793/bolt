from colorama import Fore

from src.main.cli.auxiliary.decorators.dWorkflow import workflow
from src.test.cli.tools.naabu.core.tool import Naabu


@workflow(name="plugin_name", type="recon", severity="information", confidence="confirmed")
def execute(scan_type, mode, target, config, scan_id):
    print(f'{Fore.GREEN}[INFO]{Fore.YELLOW} Port')

    port = Naabu() \
        .domain(target.split("://")[1].split("/")[0]) \
        .silent() \
        .execute().results

    return "\n".join(port), ""
