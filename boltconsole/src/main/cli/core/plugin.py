from src.main.cli.auxiliary.utils.fileSystem import create_python_package, create_file, read_file, write_file
from src.main.cli.auxiliary.utils.settingsParser import SettingParser


class Plugin:
    def __init__(self, name, scan_type):
        self.name = name
        self.scan_type = scan_type
        self.settings = SettingParser()

    def create_plugin(self):
        content = read_file('src/main/resources/boilerplate/plugin/', 'plugin.boilerplate') \
            .replace('<PLUGIN_NAME>', self.name.capitalize()) \
            .replace('<SCAN_TYPE>', self.scan_type.name)

        create_file(f'src/test/cli/plugins/{self.scan_type.name}/{self.name}/', 'workflow.py')
        write_file(f'src/test/cli/plugins/{self.scan_type.name}/{self.name}/', 'workflow.py', content)

        setting = self.settings.read_setting('INSTALLED_PLUGINS')

        new_setting = setting.copy()
        new_setting.append(self.scan_type.name + "." + self.name)
        new_setting = list(dict.fromkeys(new_setting))

        self.settings.set_setting('INSTALLED_PLUGINS', new_setting)

    def execute(self):

        if create_python_package(f'src/test/cli/plugins/{self.scan_type.name}/', self.name):
            self.create_plugin()
        else:
            override = input(f'[PLUGIN] {self.name} already exists, do you want to override? (y/n): ')
            if override == 'y':
                print(f'[PLUGIN] Overriding existing plugin {self.name}')
                self.create_plugin()
            else:
                print(f'[PLUGIN] Skipping {self.name} creation')
                return 0
