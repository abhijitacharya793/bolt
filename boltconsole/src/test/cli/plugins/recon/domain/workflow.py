from colorama import Fore

from src.main.cli.auxiliary.decorators.dWorkflow import workflow
from src.main.cli.auxiliary.utils.fileSystem import create_valid_path, create_directory
from src.test.cli.tools.custom_command.core.tool import Custom_command


@workflow(name="domain_enumeration", type="recon", severity="critical", confidence="not_confirmed")
def execute(scan_type, mode, target, config, scan_id):
    print(f'{Fore.GREEN}[INFO]{Fore.YELLOW} Domain')

    target_domain = target.split('://')[-1].split('/')[0]

    create_directory(config['execution_dir'], 'domain_enumeration')

    assetfinder = f"echo {target_domain.split('.')[-2] + '.' + target_domain.split('.')[-1]} | assetfinder --subs-only | anew {config['execution_dir']}/domain_enumeration/domains"
    findomain = f"findomain -t {target} | tee -a {config['execution_dir']}/domain_enumeration/findomains"
    append_fd = f"cat {config['execution_dir']}/domain_enumeration/findomains | anew {config['execution_dir']}/domain_enumeration/domains"
    get_hosts = f"cat {config['execution_dir']}/domain_enumeration/domains | httprobe -c 50 | anew {config['execution_dir']}/domain_enumeration/hosts"

    Custom_command().command(assetfinder).execute()
    Custom_command().command(findomain).execute()
    Custom_command().command(append_fd).execute()
    Custom_command().command(get_hosts).execute()
    out, err = Custom_command().command(f"wc -l {config['execution_dir']}/domain_enumeration/hosts").execute().results

    return "domain_enum", f"{config['execution_dir']}/domain_enumeration/hosts", "err"
