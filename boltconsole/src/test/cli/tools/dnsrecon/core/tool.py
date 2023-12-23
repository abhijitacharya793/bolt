from src.main.cli.auxiliary.utils.shell import run_command


class Dnsrecon:
    def __init__(self):
        self.results = None
        self._domain = ["-d", "DO_NOT_RUN"]
        self._dictionary = ["-D", "DO_NOT_RUN"]
        self._type = ["-t", "DO_NOT_RUN"]

    def domain(self, value=""):
        self._domain[1] = value
        return self

    def dictionary(self, value=""):
        self._dictionary[1] = value
        return self

    def type(self, value=""):
        self._type[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "dnsrecon "
        inputs = [self._domain, self._dictionary, self._type]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = [self.__class__.__name__.lower()] + list(run_command(command))
        return self
