"""
Функция max_pair()
Реализуйте функцию max_pair(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются числа
Функция должна возвращать единственное число — максимальную сумму двух соседних чисел итерируемого объекта iterable.

https://stepik.org/lesson/666563step/17?unit=664567
"""

import itertools as it


def max_pair(iterable):
    """
    >>> print(max_pair([1, 8, 2, 4, 3]))
    10
    >>> iterator = iter([1, 2, 3, 4, 5])
    >>> print(max_pair(iterator))
    9
    >>> iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])
    >>> print(max_pair(iterator))
    0
    """
    return max(map(sum, it.pairwise(iterable)))


if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
