"""
Функция take_nth()
Реализуйте функцию take_nth(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
n — натуральное число
Функция должна возвращать n-ый по счету элемент итерируемого объекта iterable. Если итерируемый объект iterable содержит менее n элементов, функция должна вернуть значение None.

https://stepik.org/lesson/666563/step/13?unit=664567
"""

import itertools


def take_nth(iterable, n):
    """
    >>> numbers = [11, 22, 33, 44, 55]
    >>> print(take_nth(numbers, 3))
    33
    >>> iterator = iter('beegeek')
    >>> print(take_nth(iterator, 4))
    g
    >>> iterator = iter('beegeek')
    >>> print(take_nth(iterator, 10))
    None
    """
    return next(itertools.islice(iterable, n-1, n), None)


if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
