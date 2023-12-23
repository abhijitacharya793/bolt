from src.main.cli.auxiliary.utils.shell import run_command

from src.config import PWD


class Burp_json:
    def __init__(self):
        self.results = None
        self._input = ["-i", "DO_NOT_RUN"]
        self._output = ["-o", "DO_NOT_RUN"]

    def input(self, value=""):
        self._input[1] = value
        return self

    def output(self, value=""):
        self._output[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "python3 " + PWD + "/src/test/resources/scripts/burpexport_json.py "
        inputs = [self._input, self._output]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = run_command(command)
        return self
