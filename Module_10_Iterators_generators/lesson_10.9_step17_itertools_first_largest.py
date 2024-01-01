"""
Функция first_largest()
Реализуйте функцию first_largest(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект, элементами которого являются целые числа
number — произвольное число
Функция должна возвращать индекс первого элемента итерируемого объекта iterable, который больше number. Если таких элементов нет, функция должна вернуть число 

https://stepik.org/lesson/666563/step/17?unit=664567
"""

import itertools as it


def first_largest(iterable, number):
    """
    >>> numbers = [10, 2, 14, 7, 7, 18, 20]
    >>> print(first_largest(numbers, 11))
    2
    >>> iterator = iter([-1, -2, -3, -4, -5])
    >>> print(first_largest(iterator, 10))
    -1
    >>> iterator = iter([18, 21, 14, 72, 73, 18, 20])
    >>> print(first_largest(iterator, 10))
    0
    """
    # res = itertools.islice(
    #     itertools.dropwhile(lambda x: x[1] < number, enumerate(iterable)), 1
    # )

    # elem = [elem for elems in res for elem in elems]
    # if not elem:
    #     return -1
    # return elem[0]

    return next(it.dropwhile(lambda x: x[1] <= number, enumerate(iterable)), [-1])[0]


if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
