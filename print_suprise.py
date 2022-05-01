import builtins
from functools import wraps


def change_print(func):
    """
    Decorator print surprise decorator before the execute of the function.
    :param func: Function to decorate.
    :return:
    """
    @wraps(func)
    def wrapped(*args):
        builtins.print("Suprise decorator:", end=' ')
        func(*args)
    return wrapped


@change_print
def print(*args):
    """
    Print function new implementation using change print decorator.
    :param args: Arguments for print.
    """
    builtins.print(*args)


if __name__ == '__main__':
    print("I did a print suprise decorator")
    print(1990)
    help(print)

