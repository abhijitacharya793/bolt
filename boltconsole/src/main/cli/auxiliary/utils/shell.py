from subprocess import Popen, PIPE, CalledProcessError

from colorama import Fore


def run_command(command):
    print(f"{Fore.GREEN}[COMMAND]{Fore.WHITE} {command.strip()}")
    try:
        process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        out, err = process.communicate()
        return out, err
    except CalledProcessError as e:
        return "Command execution failed with error code " + str(
            e.returncode) + " and returned the following output\n" + e.output
