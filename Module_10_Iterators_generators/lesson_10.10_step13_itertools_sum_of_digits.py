"""
Функция sum_of_digits()
Реализуйте функцию sum_of_digits(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются натуральные числа
Функция должна возвращать единственное число — сумму цифр всех чисел, присутствующих в итерируемом объекте iterable.

Примечание 1. Рассмотрим набор чисел 
1+3+2+0+4+1+2+2+5=20

https://stepik.org/lesson/666563/step/17?unit=664567
"""

import itertools as it


def sum_of_digits(iterable):
    """
    >>> print(sum_of_digits([13, 20, 41, 2, 2, 5]))
    20
    >>> print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
    46
    >>> print(sum_of_digits([123456789]))
    45
    """
    return sum(map(int, it.chain.from_iterable(map(str, iterable))))


if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
