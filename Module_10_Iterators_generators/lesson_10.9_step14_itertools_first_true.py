"""
Функция first_true()
Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция predicate вернула значение True. Если такого элемента нет, функция first_true() должна вернуть значение None.

Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве аргумента значения.

https://stepik.org/lesson/666563/step/13?unit=664567
"""

import itertools


def first_true(iterable, predicate):
    """
    >>> numbers = [1, 1, 1, 1, 2, 4, 5, 6]
    >>> print(first_true(numbers, lambda num: num % 2 == 0))
    2
    >>> numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])
    >>> print(first_true(numbers, lambda num: num > 10))
    100
    >>> numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)
    >>> print(first_true(numbers, None))
    69
    >>> numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 0, 10, 100, 200)
    >>> numbers_iter = filter(None, numbers)
    >>> print(first_true(numbers_iter, lambda num: num < 0))
    None
    """
    res = list(itertools.islice(filter(predicate, iterable), 1))
    if res:
        return res[0]
    return None

if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
