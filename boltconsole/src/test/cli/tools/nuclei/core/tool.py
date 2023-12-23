from src.main.cli.auxiliary.utils.shell import run_command


class Nuclei:
    def __init__(self):
        self.results = None
        self._target = ["-u", "DO_NOT_RUN"]
        self._templates = ["-t", "DO_NOT_RUN"]
        self._attack_type = ["-at", "DO_NOT_RUN"]
        self._automatic_scan = ["-as", "DO_NOT_RUN"]
        self._debug = ["-debug", "DO_NOT_RUN"]
        self._verbose = ["-v", "DO_NOT_RUN"]
        self._follow_redirects = ["-fr", "DO_NOT_RUN"]
        self._header = ["-H", "DO_NOT_RUN"]
        self._include_rr = ["-irr", "DO_NOT_RUN"]
        self._json = ["-json", "DO_NOT_RUN"]
        self._project = ["-project", "DO_NOT_RUN"]
        self._rate_limit = ["-rl", "DO_NOT_RUN"]
        self._markdown_export = ["-me", "DO_NOT_RUN"]

    def target(self, value=""):
        self._target[1] = f"\"{value}\""
        return self

    def templates(self, value=""):
        self._templates[1] = f"\"{value}\""
        return self

    def attack_type(self, value=""):
        self._attack_type[1] = value
        return self

    def automatic_scan(self, value=""):
        self._automatic_scan[1] = value
        return self

    def debug(self, value=""):
        self._debug[1] = value
        return self

    def verbose(self, value=""):
        self._verbose[1] = value
        return self

    def follow_redirects(self, value=""):
        self._follow_redirects[1] = value
        return self

    def header(self, value=""):
        self._header[1] = f"\"{value}\""
        return self

    def include_rr(self, value=""):
        self._include_rr[1] = value
        return self

    def json(self, value=""):
        self._json[1] = value
        return self

    def project(self, value=""):
        self._project[1] = value
        return self

    def rate_limit(self, value=""):
        self._rate_limit[1] = value
        return self

    def markdown_export(self, value=""):
        self._markdown_export[1] = f"\"{value}\""
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "nuclei "
        inputs = [self._target, self._templates, self._attack_type, self._automatic_scan, self._debug, self._verbose,
                  self._follow_redirects, self._header, self._include_rr, self._json, self._project, self._rate_limit,
                  self._markdown_export]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = [self.__class__.__name__.lower()] + list(run_command(command))
        return self
