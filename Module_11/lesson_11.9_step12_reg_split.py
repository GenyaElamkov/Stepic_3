"""
Функция multiple_split()
Реализуйте функцию multiple_split(), которая принимает два аргумента:

string — строка
delimiters — список строк
Функция должна разбивать строку string на подстроки, используя в качестве разделителей строки из списка delimiters, и возвращать полученный результат в виде списка.

Примечание 1. Другими словами, функция multiple_split() должна работать аналогично строковому методу split(), за тем исключением, что delimiters может содержать не единственный разделитель, а целый набор разделителей.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию multiple_split(), но не код, вызывающий ее.

https://stepik.org/lesson/699083/step/12?unit=698988
"""

import re


def multiple_split(string: str, delimiters: list[str]):
    escpt = "|".join(map(re.escape, delimiters))
    return re.split(rf"\s*(?:{escpt})\s*", string)


print(multiple_split("beegeek-python.stepik", [".", "-"]))
print(multiple_split("Timur---Arthur+++Dima****Anri", ["---", "+++", "****"]))
