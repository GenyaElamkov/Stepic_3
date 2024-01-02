"""
Функция ncycles()
Реализуйте функцию ncycles(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
times — натуральное число
Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable, зацикленных times раз.

https://stepik.org/lesson/674263/step/16?unit=672698
"""

import itertools as it


def ncycles(iterable, times):
    """
    >>> print(*ncycles([1, 2, 3, 4], 3))
    1 2 3 4 1 2 3 4 1 2 3 4
    >>> iterator = iter('bee')
    >>> print(*ncycles(iterator, 4))
    b e e b e e b e e b e e
    >>> iterator = iter([1])
    >>> print(*ncycles(iterator, 10))
    1 1 1 1 1 1 1 1 1 1
    """
    for k in it.tee(iterable, times):
        yield from k 




if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
