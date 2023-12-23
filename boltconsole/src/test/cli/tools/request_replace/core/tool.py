from src.main.cli.auxiliary.utils.shell import run_command

from src.config import PWD


class RequestReplace:
    def __init__(self):
        self.results = None
        self._input = ["-i", "DO_NOT_RUN"]
        self._working_dir = ["-w", "DO_NOT_RUN"]
        self._inject = ["-x", "DO_NOT_RUN"]
        self._part = ["-p", "DO_NOT_RUN"]
        self._append = ["-a", "DO_NOT_RUN"]

    def input(self, value=""):
        self._input[1] = value
        return self

    def working_dir(self, value=""):
        self._working_dir[1] = value
        return self

    def inject(self, value=""):
        self._inject[1] = value
        return self

    def part(self, value=""):
        self._part[1] = value
        return self

    def append(self, value=""):
        self._append[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "python3 " + PWD + "/src/test/resources/scripts/request_replace.py "
        inputs = [self._input, self._working_dir, self._inject, self._part, self._append]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = run_command(command)
        return self
