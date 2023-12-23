from colorama import Fore

from src.main.cli.auxiliary.utils.fileSystem import delete_directory, create_directory, create_valid_path
from src.main.cli.auxiliary.utils.pluginFactory import PluginFactory
from src.main.cli.auxiliary.utils.configParser import ConfigParser


class Run:
    def __init__(self, scan_type, mode, target, config, scan_id, batch, fuzz):
        self.scan_type = scan_type
        self.mode = mode
        self.target = target
        self.config = ConfigParser(config).parse_config()
        self.scan_id = scan_id
        self.batch = batch
        self.fuzz = fuzz

    def reset(self):
        """
        delete_directory(self.config['execution_dir'], "output")
        create_directory(self.config['execution_dir'], "output")
        """
        # self.config['execution_dir'] = create_valid_path(self.config['execution_dir'], "output")
        pass

    def execute(self):
        self.reset()
        print(f"{Fore.GREEN}[INFO]{Fore.CYAN} Starting scan", end=" ")
        pf = PluginFactory(self.scan_type, self.mode, self.target, self.config, self.scan_id, self.fuzz)
        # FIXME: uncomment
        print(self.config)
        # pf.get_scans_by_scan_type()
        return 1
