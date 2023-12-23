from src.main.cli.auxiliary.utils.shell import run_command


class Naabu:
    def __init__(self):
        self.results = None
        self._domain = ["-host", "DO_NOT_RUN"]
        self._port = ["-port", "DO_NOT_RUN"]
        self._silent = ["-silent", "DO_NOT_RUN"]

    def domain(self, value=""):
        self._domain[1] = value
        return self

    def port(self, value=""):
        self._port[1] = value
        return self

    def silent(self, value=""):
        self._silent[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "naabu "
        inputs = [self._domain, self._silent, self._port]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = [self.__class__.__name__.lower()] + list(run_command(command))
        return self
