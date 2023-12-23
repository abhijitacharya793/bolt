from src.main.cli.auxiliary.utils.fileSystem import create_python_package, create_file, read_file, write_file


class Tool:
    def __init__(self, name, command, parameter):
        self.name = name
        self.command = command
        # PARSE PARAMETERS
        self.parameter_methods = [p.split("|")[1] for p in parameter.split(",")]
        self.parameter_values = [p.split("|")[0] for p in parameter.split(",")]

    def create_tool(self):
        # GET BOILERPLATE
        param_string = []
        param_array_string = []
        param_method_string = []
        for param_method, param_value in zip(self.parameter_methods, self.parameter_values):
            param_method_string.append(read_file('src/main/resources/boilerplate/tool/', 'parameter_method.boilerplate') \
                                       .replace('<PARAMETER>', param_method))
            param_string.append(f'        self._{param_method} = ["{param_value}", "DO_NOT_RUN"]')
            param_array_string.append("self._" + param_method)

        content = read_file('src/main/resources/boilerplate/tool/', 'tool.boilerplate') \
            .replace('<TOOL_NAME>', self.name.capitalize()) \
            .replace('<TOOL_BINARY>', self.command) \
            .replace('<TOOL_PARAMS>', "\n".join(param_string)) \
            .replace('<TOOL_PARAM_METHOD>', "\n\n".join(param_method_string)) \
            .replace('<TOOL_PARAM_ARRAY>', f'        inputs = [{",".join(param_array_string)}]')

        # CREATE FILE
        create_python_package(f'src/test/cli/tools/{self.name}/', 'core')
        create_file(f'src/test/cli/tools/{self.name}/core/', 'tool.py')
        write_file(f'src/test/cli/tools/{self.name}/core/', 'tool.py', content)

    def execute(self):
        if create_python_package('src/test/cli/tools/', self.name):
            self.create_tool()
        else:
            override = input(f'[TOOL] {self.name} already exists, do you want to override? (y/n): ')
            if override == 'y':
                print(f'[TOOL] Overriding existing tool {self.name}')
                self.create_tool()
            else:
                print(f'[TOOL] Skipping {self.name} creation')
                return 0
