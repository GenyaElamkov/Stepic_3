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


def group_anagrams(words: str):
    """_summary_
    >>> groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
    >>> print(*groups)
    ('boko', 'book') ('evil', 'levi', 'live') ('afther', 'father')
    >>> groups = group_anagrams(['evil', 'father', 'book', 'stepik', 'beegeek'])
    >>> print(*groups)
    ('beegeek',) ('book',) ('evil',) ('father',) ('stepik',)
    >>> groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])
    >>> print(*groups)
    ('крона', 'норка') ('сеточка', 'тесачок', 'стоечка') ('лучик', 'чулки')
    """

    groub_iter = groupby(sorted(words, key=sorted), key=sorted)
    return [tuple(v) for _, v in groub_iter]


if __name__ == "__main__":      
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
