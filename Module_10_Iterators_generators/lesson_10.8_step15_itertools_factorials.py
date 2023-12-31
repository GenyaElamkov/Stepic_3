"""
Функция factorials()
Реализуйте функцию factorials() с использованием функции accumulate(), которая принимает один аргумент:

n — натуральное число
Функция должна возвращать итератор, генерирующий последовательность из n чисел, каждое из которых является факториалом очередного натурального числа.

https://stepik.org/lesson/640045/step/16?unit=636565
"""

import itertools
import operator


def factorials(n):
    """
    >>> numbers = factorials(6)
    >>> print(*numbers)
    1 2 6 24 120 720
    >>> numbers = factorials(2)

    >>> print(next(numbers))
    1
    >>> print(next(numbers))
    2
    """
    return itertools.accumulate(range(1, n+1), operator.mul)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
