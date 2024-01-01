"""
Функция take()
Реализуйте функцию take(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
n — натуральное число
Функция должна возвращать итератор, генерирующий последовательность из первых n элементов итерируемого объекта iterable.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.

https://stepik.org/lesson/666563/step/13?unit=664567
"""

import itertools


def take(iterable, n):
    """
    >>> print(*take(range(10), 5))
    0 1 2 3 4
    >>> iterator = iter('beegeek')
    >>> print(*take(iterator, 22))
    b e e g e e k
    >>> iterator = iter('beegeek')
    >>> print(*take(iterator, 1))
    b
    """
    return itertools.islice(iterable, n)


if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
