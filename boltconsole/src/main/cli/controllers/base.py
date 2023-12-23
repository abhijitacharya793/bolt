import click

from src.main.cli.auxiliary.enums.eConfidence import Confidence
from src.main.cli.auxiliary.enums.eMode import Mode
from src.main.cli.auxiliary.enums.eScanType import ScanTypes
from src.main.cli.auxiliary.enums.eSeverity import Severity
from src.main.cli.auxiliary.enums.eVulnerabilityType import VulnerabilityTypes
from src.main.cli.core.install import Install
from src.main.cli.core.plugin import Plugin
from src.main.cli.core.run import Run
from src.main.cli.core.tool import Tool

COMMANDS = {x.name[:3]: x for x in VulnerabilityTypes} | {x.name[:3]: x for x in ScanTypes} | {x.name[:3]: x for x in
                                                                                               Severity} | {
               x.name[:3]: x
               for x in
               Confidence}

MODES = {x.name[:3]: x for x in Mode}


@click.group()
def controller():
    pass


@controller.command()
@click.option("-s", "--scan_type", type=click.Choice(COMMANDS), default="inf", prompt="Enter scan type",
              help="Scan type")
@click.option("-t", "--target", prompt="Enter target base URL", help="Target base URL")
@click.option("-m", "--mode", type=click.Choice(MODES), default="fas", prompt="Enter mode",
              help="Enter mode - aggressive (a), normal (n), fast (f)")
@click.option("-c", "--config", type=click.Path(exists=True), prompt="Enter config file path", help="Config file path")
# @click.option("-ed", "--exec_dir", type=click.Path(exists=True), prompt="Enter execution directory",
#               help="Execution directory")
# @click.option("-be", "--burp_export", type=click.Path(exists=True), prompt="Enter burpsuite export file path",
#               help="Burpsuite export file path")
# @click.option("-li", "--login", type=click.Path(exists=True), prompt="Enter login file path", help="Login file path",
#               required=False)
# @click.option("-lo", "--logout", type=click.Path(exists=True), prompt="Enter logout file path", help="Logout file path",
#               required=False)
@click.option("-id", "--scan_id", default=None, required=False,
              help="Existing Scan ID")
# @click.option("-rl", "--rate_limit", prompt="Enter Rate Limit", help="Rate limit")
@click.option("-b", "--batch", is_flag=True, default=False, show_default=True,
              help="Never ask for user input, use the default behavior")
@click.option("-f", "--fuzz", is_flag=True, default=False, show_default=True, help="Fuzz for payloads")
def run(scan_type, target, mode, config, scan_id, batch, fuzz):
    """
    Ex: python3 main.py run -t test.com -s sql -c working_dir/config.json -ed working_dir
                -be working_dir/burp_export.xml -li working_dir/login -lo working_dir/logout -m fas -f -b
    """
    task = Run(COMMANDS[scan_type], MODES[mode], target, config, scan_id, batch, fuzz)
    task.execute()


@controller.command()
@click.option("-n", "--name", prompt="Enter plugin name", help="Plugin name")
@click.option("-s", "--scan_type", type=click.Choice(COMMANDS), default="inf", prompt="Enter scan type",
              help="Scan type")
def plugin(name, scan_type):
    """
    Ex: python3 main.py plugin -n xss_fuzz -s inj -m fas
    """
    task = Plugin(name, COMMANDS[scan_type])
    task.execute()


@controller.command()
@click.option("-n", "--name", prompt="Enter tool name", help="Tool name")
@click.option("-c", "--command", prompt="Enter tool execution command", help="Tool execution command")
@click.option("-p", "--parameter", prompt="Enter tool name", help="Tool name")
def tool(name, command, parameter):
    """
    Ex: python3 main.py tool -n request_replace -c "python3 /home/katsuro/Tools/bolt/resources/scripts/request_replace.py" -p "-i|input,-x|injection,-p|part"
    """
    task = Tool(name, command, parameter)
    task.execute()


@controller.command()
def install():
    """
    Ex: python3 main.py install
    """
    task = Install()
    task.execute()
