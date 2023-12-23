from src.main.cli.auxiliary.utils.shell import run_command


class Ffuf:
    def __init__(self):
        self.results = None
        self._target = ["-u", "DO_NOT_RUN"]
        self._wordlist = ["-w", "DO_NOT_RUN"]
        self._recursion = ["-recursion", "DO_NOT_RUN"]
        self._extension = ["-e", "DO_NOT_RUN"]
        self._silent = ["-s", "DO_NOT_RUN"]
        self._output_format = ["-of", "DO_NOT_RUN"]
        self._output = ["-o", "DO_NOT_RUN"]
        self._match_status_code = ["-mc", "DO_NOT_RUN"]
        self._match_lines = ["-ml", "DO_NOT_RUN"]
        self._match_regexp = ["-mr", "DO_NOT_RUN"]
        self._match_size = ["-ms", "DO_NOT_RUN"]
        self._match_words = ["-mw", "DO_NOT_RUN"]
        self._filter_status_code = ["-fc", "DO_NOT_RUN"]
        self._filter_lines = ["-fl", "DO_NOT_RUN"]
        self._filter_regexp = ["-fr", "DO_NOT_RUN"]
        self._filter_size = ["-fs", "DO_NOT_RUN"]
        self._filter_words = ["-fw", "DO_NOT_RUN"]
        self._cookies = ["-b", "DO_NOT_RUN"]
        self._headers = ["-H", "DO_NOT_RUN"]
        self._request_file = ["-request", "DO_NOT_RUN"]
        self._mode = ["-mode", "DO_NOT_RUN"]
        self._stop_on_error = ["-se", "DO_NOT_RUN"]
        self._rate = ["-rate", "DO_NOT_RUN"]
        self._replay_proxy = ["-replay-proxy", "DO_NOT_RUN"]

    def target(self, value = ""):
        self._target[1] = value
        return self

    def wordlist(self, value = ""):
        self._wordlist[1] = value
        return self

    def recursion(self, value = ""):
        self._recursion[1] = value
        return self

    def extension(self, value = ""):
        self._extension[1] = value
        return self

    def silent(self, value = ""):
        self._silent[1] = value
        return self

    def output_format(self, value = ""):
        self._output_format[1] = value
        return self

    def output(self, value = ""):
        self._output[1] = value
        return self

    def match_status_code(self, value = ""):
        self._match_status_code[1] = value
        return self

    def match_lines(self, value = ""):
        self._match_lines[1] = value
        return self

    def match_regexp(self, value = ""):
        self._match_regexp[1] = value
        return self

    def match_size(self, value = ""):
        self._match_size[1] = value
        return self

    def match_words(self, value = ""):
        self._match_words[1] = value
        return self

    def filter_status_code(self, value = ""):
        self._filter_status_code[1] = value
        return self

    def filter_lines(self, value = ""):
        self._filter_lines[1] = value
        return self

    def filter_regexp(self, value = ""):
        self._filter_regexp[1] = value
        return self

    def filter_size(self, value = ""):
        self._filter_size[1] = value
        return self

    def filter_words(self, value = ""):
        self._filter_words[1] = value
        return self

    def cookies(self, value = ""):
        self._cookies[1] = value
        return self

    def headers(self, value = ""):
        self._headers[1] = value
        return self

    def request_file(self, value = ""):
        self._request_file[1] = value
        return self

    def mode(self, value = ""):
        self._mode[1] = value
        return self

    def stop_on_error(self, value = ""):
        self._stop_on_error[1] = value
        return self

    def rate(self, value = ""):
        self._rate[1] = value
        return self

    def replay_proxy(self, value = ""):
        self._replay_proxy[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "ffuf "
        inputs = [self._target,self._wordlist,self._recursion,self._extension,self._silent,self._output_format,self._output,self._match_status_code,self._match_lines,self._match_regexp,self._match_size,self._match_words,self._filter_status_code,self._filter_lines,self._filter_regexp,self._filter_size,self._filter_words,self._cookies,self._headers,self._request_file,self._mode,self._stop_on_error,self._rate,self._replay_proxy]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        self.results = run_command(command)
        return self
