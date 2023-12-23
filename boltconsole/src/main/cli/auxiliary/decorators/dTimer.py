import time
from colorama import Fore, Back, Style


def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        if int(end - start) != 0:
            print(f'{Fore.GREEN}[INFO]{Fore.WHITE} {func.__name__} took {int((end - start))} sec')
        return result

    return wrapper
