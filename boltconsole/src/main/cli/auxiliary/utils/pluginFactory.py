from datetime import datetime
import time
from importlib import import_module

from src.main.cli.auxiliary.utils import dbUtil
from src.main.cli.settings import INSTALLED_PLUGINS

db = dbUtil.DBUtil()


class PluginFactory:
    def __init__(self, scan_type, mode, target, config, scan_id, fuzz):
        self.scan_type = scan_type
        self.mode = mode
        self.target = target
        self.config = config
        self.fuzz = fuzz
        self.scan_id = time.time() if scan_id is None else float(scan_id)

    def get_scans_by_scan_type(self):
        print(self.scan_id)
        scan_object = db.get_one("bolt_scans", {"scan_id": self.scan_id})

        if scan_object:
            db.updates("bolt_scans", scan_object["_id"], "status", "running")
        else:
            scan_object = db.insert("bolt_scans",
                                    {"scan_id": self.scan_id, "target": self.target, "application": self.config["app"],
                                     "status": "running", "date": datetime.fromtimestamp(self.scan_id)})
        for scan in INSTALLED_PLUGINS:
            from src.main.cli.auxiliary.utils.fileSystem import create_valid_path
            # SKIP FUZZING
            if "fuzz" in scan and not self.fuzz:
                continue
            elif "fuzz" not in scan and self.fuzz:
                continue
            config = self.config.copy()
            config['execution_dir'] = create_valid_path(self.config['execution_dir'],
                                                        f"output_{scan.split('.')[1][:3]}")

            scan = import_module(f'src.test.cli.plugins.{scan}.workflow')
            scan.execute(self.scan_type, self.mode, self.target, config, self.scan_id)

        db.updates("bolt_scans", scan_object["_id"], "status", "completed")
