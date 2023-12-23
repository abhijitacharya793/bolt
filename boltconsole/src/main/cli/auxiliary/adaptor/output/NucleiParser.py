import glob
import time

from src.main.cli.auxiliary.utils import dbUtil

db = dbUtil.DBUtil()


class NucleiParser:
    def __init__(self, scan_id, scan_name, config, result, error):
        self.scan_id = scan_id
        self.scan_name = scan_name
        self.result = result
        self.error = error
        self.config = config

    def get_issues(self):
        issues_identified = []
        if not self.result:
            print(self.error)
        else:
            issues = glob.glob(self.config['execution_dir'] + f"/result_{self.scan_name}/*")
            for issue in issues:
                if 'index.md' not in issue:
                    with open(issue, 'r') as f:
                        content = f.read()
                        issues_identified.append(
                            {'scan_id': self.scan_id, 'vulnerability_id': time.time(), 'plugin': self.scan_name,
                             'request': content.split("```")[1][5:],
                             'response': content.split("```")[3][5:]})
        return issues_identified

    def write_issues_to_file(self, issues):
        for issue in issues:
            with open(self.config['execution_dir'] + '/report.md', 'a') as f:
                f.write(f"# {issue['plugin']}\n")
                f.write(f"---\n")
                f.write(f"```http\n")
                f.write(f"{issue['request']}")
                f.write(f"```\n")
                f.write(f"```http\n")
                f.write(f"{issue['response']}")
                f.write(f"```\n")

    def write_issues_to_db(self, issues):
        for issue in issues:
            db.insert("vulnerabilities", issue)
