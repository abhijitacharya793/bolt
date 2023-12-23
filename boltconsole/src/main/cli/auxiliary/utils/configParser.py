import json

"""
# SAMPLE CONFIG FILE
{
    "execution_dir": "exec_bwapp",
    "login": "exec_bwapp/login",
    "logout": "",
    "burp_export": "exec_bwapp/bwapp_xmli.xml",
    "rate_limit": "10"
}
# SAMPLE FOLDER STRUCTURE
exec_bwapp
 | config.json
 | login
 | bwapp_xmli.xml
"""


# TODO: Improve config parsing, add checks
# Everytime any new config is added, it should be updated here
class Config:
    def __init__(self):
        self.execution_dir = ""
        self.login = ""
        self.logout = ""


class ConfigParser:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = None

    def parse_config(self):
        with open(self.config_path, "r") as config_json:
            self.config = json.load(config_json)
            print(self.config)
        return self.config
