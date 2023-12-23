from src.main.cli.auxiliary.utils.shell import run_command


class Findomain:
    def __init__(self):
        self.results = None
        self._domain = ["-t", "DO_NOT_RUN"]
        self._output_dir = ["-u", "DO_NOT_RUN"]

    def domain(self, value = ""):
        self._domain[1] = value
        return self

    def output_dir(self, value = ""):
        self._output_dir[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "findomain "
        inputs = [self._domain,self._output_dir]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = [self.__class__.__name__.lower()] + list(run_command(command))
        return self
