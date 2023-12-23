from src.main.cli.auxiliary.utils.shell import run_command

from src.config import PWD


class Sqlmap:
    def __init__(self):
        self.results = None
        self._url = ["-u", "DO_NOT_RUN"]
        self._request_file = ["-r", "DO_NOT_RUN"]
        self._verbose = ["-v", "DO_NOT_RUN"]
        self._agent = ["-A", "DO_NOT_RUN"]
        self._header = ["-H", "DO_NOT_RUN"]
        self._live_cookies = ["--live-cookies", "DO_NOT_RUN"]
        self._cookie = ["--cookie", "DO_NOT_RUN"]
        self._method = ["--method", "DO_NOT_RUN"]
        self._data = ["--data", "DO_NOT_RUN"]
        self._param = ["--param", "DO_NOT_RUN"]
        self._mobile = ["--mobile", "DO_NOT_RUN"]
        self._random_agent = ["--random-agent", "DO_NOT_RUN"]
        self._host = ["--host", "DO_NOT_RUN"]
        self._referer = ["--referer", "DO_NOT_RUN"]
        self._headers = ["--headers", "DO_NOT_RUN"]
        self._delay = ["--delay", "DO_NOT_RUN"]
        self._timeout = ["--timeout", "DO_NOT_RUN"]
        self._force_ssl = ["--force-ssl", "DO_NOT_RUN"]
        self._hpp = ["--hpp", "DO_NOT_RUN"]
        self._threads = ["--threads", "DO_NOT_RUN"]
        self._dbms = ["--dbms", "DO_NOT_RUN"]
        self._tamper = ["--tamper", "DO_NOT_RUN"]
        self._level = ["--level", "DO_NOT_RUN"]
        self._risk = ["--risk", "DO_NOT_RUN"]
        self._technique = ["--technique", "DO_NOT_RUN"]
        self._dbs = ["--dbs", "DO_NOT_RUN"]
        self._skip_waf = ["--skip-waf", "DO_NOT_RUN"]
        self._banner = ["--banner", "DO_NOT_RUN"]
        self._batch = ["--batch", "DO_NOT_RUN"]

    def url(self, value=""):
        self._url[1] = value
        return self

    def request_file(self, value=""):
        self._request_file[1] = value
        return self

    def verbose(self, value=""):
        self._verbose[1] = value
        return self

    def agent(self, value=""):
        self._agent[1] = value
        return self

    def header(self, value=""):
        self._header[1] = value
        return self

    def live_cookies(self, value=""):
        self._live_cookies[1] = value
        return self

    def cookie(self, value=""):
        self._cookie[1] = value
        return self

    def method(self, value=""):
        self._method[1] = value
        return self

    def data(self, value=""):
        self._data[1] = value
        return self

    def param(self, value=""):
        self._param[1] = value
        return self

    def mobile(self, value=""):
        self._mobile[1] = value
        return self

    def random_agent(self, value=""):
        self._random_agent[1] = value
        return self

    def host(self, value=""):
        self._host[1] = value
        return self

    def referer(self, value=""):
        self._referer[1] = value
        return self

    def headers(self, value=""):
        self._headers[1] = value
        return self

    def delay(self, value=""):
        self._delay[1] = value
        return self

    def timeout(self, value=""):
        self._timeout[1] = value
        return self

    def force_ssl(self, value=""):
        self._force_ssl[1] = value
        return self

    def hpp(self, value=""):
        self._hpp[1] = value
        return self

    def threads(self, value=""):
        self._threads[1] = value
        return self

    def dbms(self, value=""):
        self._dbms[1] = value
        return self

    def tamper(self, value=""):
        self._tamper[1] = value
        return self

    def level(self, value=""):
        self._level[1] = value
        return self

    def risk(self, value=""):
        self._risk[1] = value
        return self

    def technique(self, value=""):
        self._technique[1] = value
        return self

    def dbs(self, value=""):
        self._dbs[1] = value
        return self

    def skip_waf(self, value=""):
        self._skip_waf[1] = value
        return self

    def banner(self, value=""):
        self._banner[1] = value
        return self

    def batch(self, value=""):
        self._batch[1] = value
        return self

    @staticmethod
    def join_inputs(strings_tuple) -> str:
        if strings_tuple[1] != "DO_NOT_RUN":
            return ' '.join(strings_tuple)
        else:
            return ''

    def execute(self):
        command = "python3 " + PWD + "/../sqlmap/sqlmap.py "
        inputs = [self._url, self._request_file, self._verbose, self._agent, self._header, self._live_cookies,
                  self._cookie, self._method, self._data, self._param, self._mobile, self._random_agent, self._host,
                  self._referer, self._headers, self._delay, self._timeout, self._force_ssl, self._hpp, self._threads,
                  self._dbms, self._tamper, self._level, self._risk, self._technique, self._dbs, self._skip_waf,
                  self._banner, self._batch]
        command += ' '.join(list(map(self.join_inputs, inputs)))
        # self.results = [self.__class__.__name__.lower()] + list(run_command(command))
        self.results = run_command(command)
        return self
