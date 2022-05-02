from decimal import Decimal
from functools import lru_cache
from functools import singledispatch


@lru_cache(maxsize=None)
def fib_series(num1, num2, n):
    """
    Fibonacci series calculator, the function get the 2 first number of the series, than calculate each new number
        to be the sum of the 2 numbers before him.
        Using lru_cache for save the calls we already did for save run time to the program.
    :param num1: The first number of Fibonacci series.
    :param num2: The secend number of Fibonacci series.
    :param n:
    :return: The sum of the n number, calculate it by Fibonacci when each number is the result of the 2 numbers
        before him.
    """
    if n == 1:
        return num1
    if n == 2:
        return num2
    return fib_series(num1, num2, n - 1) + fib_series(num1, num2, n - 2)


class Animal:
    """
    Animal class: Represent abstract class of animals.
    :param height: height of the animal.
    """
    def __init__(self, height):
        self.height = height


class Dog(Animal):
    """
    Dog class: inheritance from animal, have sound.
    :param height: height of the Dog.
    """
    SOUND = "Bark"

    def __init__(self, height):
        super().__init__(height)

    @classmethod
    def get_sound(cls):
        """
        Get dog sound.
        :return: Class attribute of sound.
        """
        print("Dog Sound is:" + cls.SOUND)


class Cat(Animal):
    """
    Cat class: inheritance from animal.
    :param height: height of the Cat.
    """
    def __init__(self, height):
        super().__init__(height)


@singledispatch
def my_swap(arg1, arg2):
    """
    The function get 2 numbers and swap if the first argument is bigger than the second.
    :param arg1: number
    :param arg2: number
    """
    print("Before swap: arg1 = " + str(arg1) + " arg2 = " + str(arg2))
    if arg1 > arg2:
        arg1, arg2 = arg2, arg1
    print("After swap: arg1 = " + str(arg1) + " arg2 = " + str(arg2))


@my_swap.register(Animal)
def _(arg1, arg2):
    print("Before swap: arg1 = " + str(arg1.height) + " arg2 = " + str(arg2.height))
    if arg1.height > arg2.height:
        arg1, arg2 = arg2, arg1
    print("After swap: arg1 = " + str(arg1.height) + " arg2 = " + str(arg2.height))


if __name__ == '__main__':
    #  1) @lru_cache decorator
    print("@lru_cache decorator fibonacci series:")
    print(fib_series(3, 7, 1))
    print(fib_series(3, 7, 2))
    print(fib_series(3, 7, 3))
    print(fib_series(3, 7, 4))
    print(fib_series(3, 7, 300))
    print("-" * 50)

    #  2) @singledispatch
    print("@singledispatch swap different objects:")
    a = Animal(2)
    d = Dog(5)
    c = Cat(3)
    my_swap(1, 2)
    my_swap(2.6, 1.2)
    my_swap("db", "bc")
    my_swap(c, d)
    print("-" * 50)

    #  3)@classmethod
    print("@classmethod:")
    Dog.get_sound()


