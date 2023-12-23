from colorama import Fore

from src.main.cli.auxiliary.decorators.dWorkflow import workflow


@workflow(name="plugin_name", type="recon", severity="information", confidence="confirmed")
def execute(scan_type, mode, target, config, scan_id):
    print(f'{Fore.GREEN}[INFO]{Fore.YELLOW} Manual Information')

    # CALL TOOLS
    tenant = (input(f'{Fore.GREEN}[INPUT]{Fore.RED} [Site Structure]{Fore.WHITE} '
                    f'Multi-Tenant/Single-Tenant/Unknown (m/s/U): ') or 'u') \
        .lower()

    return tenant, ""
