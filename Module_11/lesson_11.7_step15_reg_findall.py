"""
Функция abbreviate()
Аббревиатура — слово, образованное сокращением слова или словосочетания и читаемое по алфавитному названию начальных букв или по начальным звукам слов, входящих в него.

Реализуйте функцию abbreviate(), которая принимает один аргумент:

phrase — фраза
Функция должна создавать из фразы phrase аббревиатуру в верхнем регистре и возвращать её.

Примечание 1. В аббревиатуре должны присутствовать как начальные буквы слов, так и начальные буквы подслов, начинающихся с заглавной буквы, например, JavaScript Object Notation -> JSON.

https://stepik.org/lesson/640164/step/6?unit=636683
"""

import re


def abbreviate(phrase: str) -> str:
    match = re.findall(r"\b[A-Za-z]|\B[A-Z]", phrase)
    return "".join(match).upper()


print(abbreviate("javaScript object notation"))
print(abbreviate("frequently asked questions"))
