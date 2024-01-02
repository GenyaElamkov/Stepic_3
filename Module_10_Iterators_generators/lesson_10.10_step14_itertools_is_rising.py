"""
  Функция is_rising()
Реализуйте функцию is_rising(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются числа
Функция должна возвращать True, если элементы итерируемого объекта расположены строго по возрастанию, или False в противном случае.

https://stepik.org/lesson/666563/step/17?unit=664567
"""

import itertools as it


def is_rising(iterable):
    """
    >>> print(is_rising([1, 2, 3, 4, 5]))
    True
    >>> iterator = iter([1, 1, 1, 2, 3, 4])
    >>> print(is_rising(iterator))
    False
    >>> iterator = iter(list(range(100, 200)))
    >>> print(is_rising(iterator))
    True
    """
    for chap in it.pairwise(iterable):
        if chap[0] >= chap[1]:
            return False
    return True


if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
