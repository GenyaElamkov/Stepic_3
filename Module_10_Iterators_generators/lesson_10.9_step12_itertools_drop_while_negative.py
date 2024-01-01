"""
Функция drop_while_negative()
Реализуйте функцию drop_while_negative(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются целые числа
Функция должна возвращать итератор, генерирующий все числа итерируемого объекта iterable, начиная с первого неотрицательного числа.


https://stepik.org/lesson/640045/step/16?unit=636565
"""

import itertools


def drop_while_negative(iterable):
    """Функция возвращает итератор, генерирующий все числа
      итерируемого объекта iterable, начиная с первого неотрицательного числа.

    Args:
        iterable (Any): итерируемый объект
        return: итератор

    >>> numbers = [-3, -2, -1, 0, 1, 2, 3]
    >>> print(*drop_while_negative(numbers))
    0 1 2 3

    >>> iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])
    >>> print(*drop_while_negative(iterator))
    0 1 2 3 -4 -5 -6

    >>> iterator = iter([-3, -2, -1, -4, -5, -6])
    >>> print(list(drop_while_negative(iterator)))
    []
    """
    return itertools.dropwhile(lambda x: x < 0, iterable)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
