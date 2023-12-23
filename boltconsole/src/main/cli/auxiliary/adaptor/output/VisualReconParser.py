import os
import time

from src.main.cli.auxiliary.utils import dbUtil

db = dbUtil.DBUtil()


class VisualReconParser:
    def __init__(self, scan_id, scan_name, config, result, error):
        self.scan_id = scan_id
        self.scan_name = scan_name
        self.result = result
        self.error = error
        self.config = config

    def get_issues(self):
        result = {}
        if not self.result:
            print(self.error)
        else:
            result = {'scan_id': self.scan_id, 'visual_recon_id': time.time(), 'plugin': self.scan_name,
                      "visual_recon_out": os.getcwd() + "/" + self.result + "/aquatone_report.html"}
        return result

    def write_issues_to_file(self, issues):
        # TODO:
        # for issue in issues:
        #     with open(self.config['execution_dir'] + '/report.md', 'a') as f:
        #         f.write(f"# {issue['plugin']}\n")
        #         f.write(f"---\n")
        #         f.write(f"\n```http\n")
        #         f.write(f"{issue['payload']}")
        #         f.write(f"\n```\n")
        pass

    def write_issues_to_db(self, recon):
        db.insert("visual_recon", recon)
