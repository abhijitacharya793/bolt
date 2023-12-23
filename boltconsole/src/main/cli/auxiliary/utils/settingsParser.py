from src.main.cli.auxiliary.utils.fileSystem import read_file, write_file
from src.main.cli.settings import *


# Import -> from src.main.cli.settings import *


class SettingParser:

    def read_setting(self, r_setting):
        setting_value = eval(r_setting)
        return setting_value

    def set_setting(self, setting_key, value):
        content = read_file('src/main/cli/', 'settings.py')
        current_value = self.read_setting(setting_key)
        content = content.replace(str(current_value), str(value))
        write_file('src/main/cli/', 'settings.py', content)
