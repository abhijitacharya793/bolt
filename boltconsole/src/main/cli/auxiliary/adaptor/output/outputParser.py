from src.main.cli.auxiliary.adaptor.output.DalfoxParser import DalfoxParser
from src.main.cli.auxiliary.adaptor.output.DomainParser import DomainParser
from src.main.cli.auxiliary.adaptor.output.NucleiParser import NucleiParser
from src.main.cli.auxiliary.adaptor.output.SqlmapParser import SqlmapParser
from src.main.cli.auxiliary.adaptor.output.VisualReconParser import VisualReconParser


def write_issues(detail_parser):
    results = detail_parser.get_issues()

    detail_parser.write_issues_to_file(results)
    detail_parser.write_issues_to_db(results)

    return results


def parse_output(scan_name, tool, config, result, error, scan_id):
    if tool == "sqlmap":
        detail_parser = SqlmapParser(scan_id, scan_name, config, result, error)
        results = write_issues(detail_parser)
    elif tool == "nuclei":
        detail_parser = NucleiParser(scan_id, scan_name, config, result, error)
        results = write_issues(detail_parser)
    elif tool == "dalfox":
        detail_parser = DalfoxParser(scan_id, scan_name, config, result, error)
        results = write_issues(detail_parser)
    elif tool == "domain_enum":
        detail_parser = DomainParser(scan_id, scan_name, config, result, error)
        results = write_issues(detail_parser)
    elif tool == "visual_recon":
        detail_parser = VisualReconParser(scan_id, scan_name, config, result, error)
        results = write_issues(detail_parser)
    else:
        print(tool, result, error)
        results = ""

    return results
