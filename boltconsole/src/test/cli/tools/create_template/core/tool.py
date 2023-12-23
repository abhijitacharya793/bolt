from src.main.cli.auxiliary.utils.shell import run_command

from src.config import PWD


class Create_template:
    def __init__(self):
        self.results = None
        self._template = ["-t", "DO_NOT_RUN"]
        self._working_dir = ["-w", "DO_NOT_RUN"]
        self._output = ["-o", "DO_NOT_RUN"]
        self._requests = ["-r", "DO_NOT_RUN"]

    def template(self, value=""):
        self._template[1] = value
        return self

    def working_dir(self, value=""):
        self._working_dir[1] = value
        return self

    def output(self, value=""):
        self._output[1] = value
        return self

    def requests(self, value=""):
        self._requests[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "python3 " + PWD + "/src/test/resources/scripts/create_template.py "
        inputs = [self._template, self._working_dir, self._output, self._requests]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = run_command(command)
        return self
