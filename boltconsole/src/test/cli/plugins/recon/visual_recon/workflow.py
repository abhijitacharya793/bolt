from colorama import Fore

from src.main.cli.auxiliary.decorators.dWorkflow import workflow
from src.test.cli.tools.custom_command.core.tool import Custom_command


@workflow(name="domain_enumeration", type="recon", severity="critical", confidence="not_confirmed")
def execute(scan_type, mode, target, config, scan_id):
    print(f'{Fore.GREEN}[INFO]{Fore.YELLOW} Visual_recon')

    # aquatone = f"cat {config['execution_dir']}/domain_enumeration/hosts | aquatone --chrome-path /snap/bin/chromium -out {config['execution_dir']}/domain_enumeration/aquatone_out"
    aquatone = f"cat {config['execution_dir']}/../output_dom/domain_enumeration/hosts | aquatone -out {config['execution_dir']}/domain_enumeration/aquatone_out"

    out, err = Custom_command().command(aquatone).execute().results

    # return "visual_recon", out, err
    return "visual_recon", f"{config['execution_dir']}/domain_enumeration/aquatone_out", None
