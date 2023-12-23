import os
import shutil


def create_valid_path(path, name):
    return os.path.join(path, name)


def create_directory(path, name):
    if os.path.exists(create_valid_path(path, name)):
        return 0
    os.mkdir(create_valid_path(path, name))
    return 1


def delete_directory(path, name):
    if os.path.exists(create_valid_path(path, name)):
        shutil.rmtree(create_valid_path(path, name), ignore_errors=True)
        return 1
    else:
        return 0


def create_file(path, name):
    if os.path.exists(create_valid_path(path, name)):
        return 0
    with open(create_valid_path(path, name), "w"):
        pass
    return 1


def write_file(path, name, content):
    with open(create_valid_path(path, name), "w") as f:
        f.write(content)
    return 1


def read_file(path, name):
    with open(create_valid_path(path, name), "r") as f:
        content = f.read()
    return content


def delete_file(path, name):
    if os.path.exists(create_valid_path(path, name)):
        os.remove(create_valid_path(path, name))
        return 1
    else:
        return 0


def create_python_package(path, name):
    if create_directory(path, name):
        create_file(path + name + "/", "__init__.py")
        return 1
    else:
        return 0
