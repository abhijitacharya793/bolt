from src.main.cli.auxiliary.utils.shell import run_command


class Custom_command:
    def __init__(self):
        self.results = None
        self._command = ["", "DO_NOT_RUN"]

    def command(self, value=""):
        self._command[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = " "
        inputs = [self._command]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = run_command(command)
        return self
