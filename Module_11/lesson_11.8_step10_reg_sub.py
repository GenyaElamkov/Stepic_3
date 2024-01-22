"""
Функция normalize_whitespace()
Реализуйте функцию normalize_whitespace(), которая принимает один аргумент:

string — произвольная строка
Функция должна заменять все множественные пробелы в строке string на единственный пробел и возвращать полученный результат.

https://stepik.org/lesson/680266/step/10?unit=678924
"""

import re


def normalize_whitespace(string):
    return re.sub(r"\s{2,}", r" ", string)


print(normalize_whitespace("AAAA                A                AAAA"))
