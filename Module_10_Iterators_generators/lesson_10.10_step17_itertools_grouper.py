"""
Функция grouper()
Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
n — натуральное число
Функция должна возвращать итератор, генерирующий последовательность, элементами которой являются объединенные в кортежи по n элементов соседние элементы итерируемого объекта iterable. Если у элемента не достаточно соседей, то ими становится значение None.

https://stepik.org/lesson/674263/step/16?unit=672698
"""

import itertools as it


def grouper(iterable, n):
    """
    >>> numbers = [1, 2, 3, 4, 5, 6]
    >>> print(*grouper(numbers, 2))
    (1, 2) (3, 4) (5, 6)
    >>> iterator = iter([1, 2, 3, 4, 5, 6, 7])
    >>> print(*grouper(iterator, 3))
    (1, 2, 3) (4, 5, 6) (7, None, None)
    >>> iterator = iter([1, 2, 3])
    >>> print(*grouper(iterator, 5))
    (1, 2, 3, None, None)
    """
    return it.zip_longest(*it.repeat(iter(iterable), n))


if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
