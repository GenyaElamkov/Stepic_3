"""
Функция normalize_jpeg()
Реализуйте функцию normalize_jpeg(), которая принимает один аргумент:

filename — название файла, имеющее расширение jpeg или jpg, которое может быть записано буквами произвольного регистра
Функция должна возвращать новое название файла с нормализованным расширением — jpg.

https://stepik.org/lesson/680266/step/9?unit=678924
"""

import re


def normalize_jpeg(filename):
    return re.sub(r"\.\w+$", r".jpg", filename, flags=re.I)


print(normalize_jpeg("stepik.jPeG"))
