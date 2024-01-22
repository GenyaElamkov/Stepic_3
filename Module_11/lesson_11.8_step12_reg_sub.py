"""
Первые буквы
Напишите программу, которая меняет местами первые две буквы в каждом слове, состоящем из двух или более букв.

Формат входных данных
На вход программе подается строка, содержащая слова.

Формат выходных данных
Программа должна в введенной строке заменить первые две буквы в каждом слове, состоящем из двух или более букв, и вывести полученный результат.

Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, соответствующими \W.

https://stepik.org/lesson/680266/step/12?unit=678924
"""

import re
import keyword


def res(text):
    kwlist = keyword.kwlist
    for word in kwlist:
        text = re.sub(rf"\b{word}\b", r"<kw>", text, flags=re.I)
    return text

print(res(input()))
