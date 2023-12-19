"""
Функция all_together()
Реализуйте функцию all_together() с использованием генераторных выражений, которая принимает произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом.

Функция должна возвращать генератор, порождающий каждый элемент всех переданных итерируемых объектов: сначала все элементы первого итерируемого объекта, затем второго, и так далее.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

https://stepik.org/lesson/640049/step/18?unit=636569
"""

from typing import Generator, Any

def all_together(*args) -> Generator[Any, None, None]:
    # return (elm for elems in args for elm in elems)
    for elem in args:
        yield from elem
        


objects = [range(3), "bee", [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))
