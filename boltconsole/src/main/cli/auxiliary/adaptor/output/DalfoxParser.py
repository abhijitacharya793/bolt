import time

from src.main.cli.auxiliary.utils import dbUtil

db = dbUtil.DBUtil()


class DalfoxParser:
    def __init__(self, scan_id, scan_name, config, result, error):
        self.scan_id = scan_id
        self.scan_name = scan_name
        self.result = result
        self.error = error
        self.config = config

    def get_issues(self):
        # TODO: Get scan_id, scan, request, response, payload
        issues_identified = []
        if not self.result:
            print(self.error)
        else:
            for issue in self.result:
                output = issue[0]
                print(output)
                # request = output.split('[#1]:\n')[1].split("\n\n")[0]
                # response = output.split('[#1] ')[1].split("</html>\n")[0].rsplit("}\n", 1)[0]
                # payload = ''
                issues_identified.append(
                    {'scan_id': self.scan_id, 'vulnerability_id': time.time(), 'plugin': self.scan_name,
                     'payload': output})

        return issues_identified

    def write_issues_to_file(self, issues):
        for issue in issues:
            with open(self.config['execution_dir'] + '/report.md', 'a') as f:
                f.write(f"# {issue['plugin']}\n")
                f.write(f"---\n")
                f.write(f"\n```http\n")
                f.write(f"{issue['payload']}")
                f.write(f"\n```\n")

    def write_issues_to_db(self, issues):
        for issue in issues:
            db.insert("vulnerabilities", issue)
