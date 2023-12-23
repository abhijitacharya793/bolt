from src.main.cli.auxiliary.utils.shell import run_command


class Getjs:
    def __init__(self):
        self.results = None
        self._input = ["-input", "DO_NOT_RUN"]
        self._no_color = ["--nocolors", "DO_NOT_RUN"]
        self._complete = ["--complete", "DO_NOT_RUN"]
        self._header = ["--header", "DO_NOT_RUN"]
        self._insecure = ["--insecure", "DO_NOT_RUN"]
        self._output = ["--output", "DO_NOT_RUN"]

    def input(self, value = ""):
        self._input[1] = value
        return self

    def no_color(self, value = ""):
        self._no_color[1] = value
        return self

    def complete(self, value = ""):
        self._complete[1] = value
        return self

    def header(self, value = ""):
        self._header[1] = value
        return self

    def insecure(self, value = ""):
        self._insecure[1] = value
        return self

    def output(self, value = ""):
        self._output[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "getJS "
        inputs = [self._input,self._no_color,self._complete,self._header,self._insecure,self._output]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = [self.__class__.__name__.lower()] + list(run_command(command))
        return self
