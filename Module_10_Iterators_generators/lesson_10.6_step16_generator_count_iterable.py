"""
Функция count_iterable()
Реализуйте функцию count_iterable() с использованием генераторных выражений, которая принимает один аргумент:

iterable — итерируемый объект
Функция должна возвращать единственное число — количество элементов итерируемого объекта iterable.

Примечание 1. Гарантируется, что передаваемый в функцию итерируемый объект является конечным.

https://stepik.org/lesson/640049/step/17?unit=636569
"""


def count_iterable(iterable) -> int:
    return sum(True for _ in iterable)


data = tuple(range(432, 3845, 17))

print(count_iterable(data))