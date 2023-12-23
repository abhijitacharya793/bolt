from src.main.cli.auxiliary.utils.shell import run_command


class Dalfox:
    def __init__(self):
        self.results = None
        self._mode = ["", "DO_NOT_RUN"]
        self._request_file = ["--rawdata", "DO_NOT_RUN"]
        self._http = ["", "DO_NOT_RUN"]
        self._silent = ["--silence", "DO_NOT_RUN"]
        self._no_color = ["--no-color", "DO_NOT_RUN"]
        self._cookie = ["--cookie", "DO_NOT_RUN"]
        self._proxy = ["--proxy", "DO_NOT_RUN"]

    def mode(self, value=""):
        self._mode[1] = value
        return self

    def request_file(self, value=""):
        self._request_file[1] = value
        return self

    def http(self, value=""):
        self._http[1] = value
        return self

    def silent(self, value=""):
        self._silent[1] = value
        return self

    def no_color(self, value=""):
        self._no_color[1] = value
        return self

    def cookie(self, value=""):
        self._cookie[1] = value
        return self

    def proxy(self, value=""):
        self._proxy[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "dalfox "
        inputs = [self._mode, self._request_file, self._http, self._silent, self._no_color, self._cookie, self._proxy]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = run_command(command)
        return self
