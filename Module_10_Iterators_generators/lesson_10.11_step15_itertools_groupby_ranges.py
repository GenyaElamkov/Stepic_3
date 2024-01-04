"""
Функция group_anagrams()
Анаграммы — это слова, которые состоят из одинаковых букв. Например:

адаптер — петарда
адресочек — середочка
азбука — базука
аистенок — осетинка
Реализуйте функцию group_anagrams(), которая принимает один аргумент:

words — список слов
Функция должна группировать в кортежи слова из списка words, являющиеся анаграммами, и возвращать список полученных кортежей.

https://stepik.org/lesson/674263/step/16?unit=672698
"""

from itertools import groupby


def ranges(numbers: list[int]):
    """
    >>> numbers = [1, 2, 3, 4, 7, 8, 10]
    >>> print(ranges(numbers))
    [(1, 4), (7, 8), (10, 10)]
    >>> numbers = [1, 3, 5, 7]
    >>> print(ranges(numbers))
    [(1, 1), (3, 3), (5, 5), (7, 7)]
    >>> numbers = [1, 2, 3, 4, 5, 6, 7]
    >>> print(ranges(numbers))
    [(1, 7)]
    """
    groub_iter = groupby(numbers, key=lambda x: numbers.index(x) - x)

    arr = []
    for _, v in groub_iter:
        res = list(v)
        arr.append((res[0], res[-1]))
    return arr


if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
