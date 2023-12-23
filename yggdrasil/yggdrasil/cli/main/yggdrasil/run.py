import time

from rich import print
from importlib import import_module
from rich.progress import Progress, SpinnerColumn, TextColumn


class Run:
    def __init__(self, scan, power, api):
        self.scan = scan
        self.power = power
        self.api = api

    def reset(self):
        pass

    def execute(self):
        self.reset()
        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
        ) as progress:
            progress.add_task(description="Scanning API...", total=None)
            # scan = import_module(f'src.test.cli.plugins.{self.scan}.workflow')
            # scan.execute(self.api, self.power)
        print("Done!")

        return 1
