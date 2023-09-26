"""
Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем порядке:

ordered_dict — словарь OrderedDict
by_values — булево значение, по умолчанию имеет значение False
Функция должна сортировать словарь ordered_dict:

по ключам, если by_values имеет значение False
по значениям, если by_values имеет значение True

https://stepik.org/lesson/634520/step/19?unit=630783
"""

from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    if not by_values:
        res = sorted(ordered_dict)
    else:
        res = sorted(ordered_dict, key=ordered_dict.get)

    for k in res:
        ordered_dict.move_to_end(k)
    return ordered_dict


data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(data.items())
