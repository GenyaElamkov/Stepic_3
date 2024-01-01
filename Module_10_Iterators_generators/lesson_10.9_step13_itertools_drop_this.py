"""
Функция drop_this()
Реализуйте функцию drop_this(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
obj — произвольный объект
Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable, начиная с элемента, не равного obj.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.

https://stepik.org/lesson/666563/step/13?unit=664567
"""

import itertools


def drop_this(iterable, obj):
    """
    >>> numbers = [0, 0, 0, 1, 2, 3]
    >>> print(*drop_this(numbers, 0))
    1 2 3
    >>> iterator = iter('bbbbeebee')
    >>> print(*drop_this(iterator, 'b'))
    e e b e e
    >>> iterator = iter('ssssssssssssssssssssssss')
    >>> print(list(drop_this(iterator, 's')))
    []
    """
    return itertools.dropwhile(lambda x: x == obj, iterable)


if __name__ == "__main__":
    import doctest
    print('\nSTART')
    doctest.testmod()
    print('END')