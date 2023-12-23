import time

from src.main.cli.auxiliary.utils import dbUtil

db = dbUtil.DBUtil()


class DomainParser:
    def __init__(self, scan_id, scan_name, config, result, error):
        self.scan_id = scan_id
        self.scan_name = scan_name
        self.result = result
        self.error = error
        self.config = config

    def get_issues(self):
        domains_identified = []
        if not self.result:
            print(self.error)
        else:
            # READ HOSTS FILE
            with open(self.result) as host_file:
                hosts = host_file.read().split("\n")
            for host in hosts:
                domains_identified.append(
                    {'scan_id': self.scan_id, 'host_id': time.time(), 'plugin': self.scan_name,
                     'host': host})

        return domains_identified

    def write_issues_to_file(self, issues):
        # TODO: Add to report
        # for issue in issues:
        #     with open(self.config['execution_dir'] + '/report.md', 'a') as f:
        #         f.write(f"# {issue['plugin']}\n")
        #         f.write(f"---\n")
        #         f.write(f"\n```http\n")
        #         f.write(f"{issue['payload']}")
        #         f.write(f"\n```\n")
        pass

    def write_issues_to_db(self, hosts):
        for host in hosts:
            db.insert("domains", host)
