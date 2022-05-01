from functools import wraps


class InvalidTypeFunctionValue(Exception):
    pass


def checktype(data_type):
    """
    checktype
    :param data_type:
    :return:
    """
    @wraps(data_type)
    def wrapper(func):
        """
        wrapper
        :param func:
        :return:
        """
        @wraps(func)
        def wrapper2(*args):
            """
            wrapper 2
            :param args:
            :return:
            """
            if type(func(*args)) != data_type:
                raise InvalidTypeFunctionValue
            return func(*args)
        return wrapper2
    return wrapper


@checktype(str)
def times(num):
    """
    Math function multiply the given number by 2.
    :param num:
    :return: num multiply by 2.
    """
    return num*2


@checktype(float)
def times2(num):
    return num / 2


if __name__ == '__main__':
    try:
        print(times(2))
    except InvalidTypeFunctionValue:
        print("Error, the function return different type.")
    try:
        print(times2(2))
    except InvalidTypeFunctionValue:
        print("Error, the function return different type.")


