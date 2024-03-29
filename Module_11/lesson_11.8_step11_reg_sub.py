"""
Ключевые слова
В Python существуют ключевые слова, которые нельзя использовать для названия переменных, функций и классов. Для получения списка всех ключевых слов можно воспользоваться атрибутом kwlist из модуля keyword.

Приведенный ниже код:

import keyword

print(keyword.kwlist)
выводит:

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>.

https://stepik.org/lesson/680266/step/11?unit=678924
"""

import re
import keyword


def res(text):
    kwlist = keyword.kwlist
    for word in kwlist:
        text = re.sub(rf"\b{word}\b", r"<kw>", text, flags=re.I)
    return text

print(res(input()))
