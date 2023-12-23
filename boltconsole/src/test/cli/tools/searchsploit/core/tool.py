from src.main.cli.auxiliary.utils.shell import run_command


class Searchsploit:
    def __init__(self):
        self.results = None
        self._list_exploits = ["", "DO_NOT_RUN"]
        self._www = ["-w", "DO_NOT_RUN"]
        self._cve = ["--cve", "DO_NOT_RUN"]
        self._verbose = ["-v", "DO_NOT_RUN"]
        self._disable_color = ["--disable-color", "DO_NOT_RUN"]
        self._update = ["--update", "DO_NOT_RUN"]
        self._check_nmap_results = ["--nmap", "DO_NOT_RUN"]

    def list_exploits(self, value=""):
        self._list_exploits[1] = value
        return self

    def www(self, value=""):
        self._www[1] = value
        return self

    def cve(self, value=""):
        self._cve[1] = value
        return self

    def verbose(self, value=""):
        self._verbose[1] = value
        return self

    def disable_color(self, value=""):
        self._disable_color[1] = value
        return self

    def update(self, value=""):
        self._update[1] = value
        return self

    def check_nmap_results(self, value=""):
        self._check_nmap_results[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "searchsploit "
        inputs = [self._list_exploits, self._www, self._cve, self._verbose, self._disable_color, self._update,
                  self._check_nmap_results]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = [self.__class__.__name__.lower()] + list(run_command(command))
        return self
