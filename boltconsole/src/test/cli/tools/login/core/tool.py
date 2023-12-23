from src.main.cli.auxiliary.utils.shell import run_command

from src.config import PWD


class Login:
    def __init__(self):
        self.results = None
        self._json_file = ["-j", "DO_NOT_RUN"]

    def json_file(self, value=""):
        self._json_file[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "python3 " + PWD + "/src/test/resources/scripts/login.py "
        inputs = [self._json_file]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = run_command(command)
        return self
