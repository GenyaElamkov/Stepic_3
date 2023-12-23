"""
Функция filter_names()
Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:

names — список имен
ignore_char — одиночный символ
max_names — натуральное число
Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые

начинаются на ignore_char (в любом регистре)
содержат хотя бы одну цифру
Если max_names больше количества имен в списке names, то генератор должен породить все возможные имена из данного списка. 

Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

https://stepik.org/lesson/673155/step/7?unit=671418
"""


from typing import Any, Generator


def filter_names(names: list[str], ignore_char: str, max_names: int) -> Generator[str, Any, None]:
    counter = 0
    for name in names:
        if name.lower().startswith(ignore_char.lower()):
            continue
        if any(map(str.isdigit, name)):
            continue
        if counter < max_names:
            counter += 1
            yield name


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))