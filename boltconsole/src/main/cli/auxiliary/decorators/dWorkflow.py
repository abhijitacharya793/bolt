from src.main.cli.auxiliary.adaptor.output.outputParser import parse_output
from src.main.cli.auxiliary.decorators.dTimer import timer
from src.main.cli.auxiliary.enums.eScanType import ScanTypes
from src.main.cli.auxiliary.enums.eSeverity import Severity
from src.main.cli.auxiliary.enums.eToolType import ToolTypes
from src.main.cli.auxiliary.enums.eConfidence import Confidence
from src.main.cli.auxiliary.enums.eVulnerabilityType import VulnerabilityTypes


def skip():
    pass


@timer
def scan(func, *args):
    tool, out, err = func(*args)
    config = args[3]
    scan_id = args[4]

    result = parse_output(func.__module__.split(".")[5], tool, config, out, err, scan_id)
    return result


def execute_function_by_decorator(func, name, scan_type_enum, severity, confidence, *args):
    if args[0] == name or args[0] == scan_type_enum or args[0] == ScanTypes.all or args[0] == severity or args[
        0] == confidence:
        return scan(func, *args)
    else:
        return skip()


def workflow(*args, **kwargs):
    def inner(func):
        def wrapper(*w_args):
            result = execute_function_by_decorator(
                func,
                eval(f"VulnerabilityTypes.{kwargs['name'].lower()}"),
                eval(f"ScanTypes.{kwargs['type'].lower()}"),
                eval(f"Severity.{kwargs['severity'].lower()}"),
                eval(f"Confidence.{kwargs['confidence'].lower()}"),
                *w_args
            )
            return result

        return wrapper

    return inner
