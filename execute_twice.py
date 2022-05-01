import builtins

import decorator


@decorator.decorator
def execute_twice(func, *args):
    """
    Decorator for execute the given function 2 times.
    :param func: Decorator given function.
    """
    func(*args)
    func(*args)


@execute_twice
def print(*args):
    """
    New implementation for Print function, adding execute_twice decorator.
    :param args: Arguments for print.
    """
    builtins.print(*args)


if __name__ == '__main__':
    print("Task 3 is finish.")
