"""
Функция unique()
Реализуйте генераторную функцию, которая принимает один аргумент:

iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable без дубликатов.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

https://stepik.org/lesson/673155/step/11?unit=671418
"""


def unique(iterable):
    elems = set()
    for elem in iterable:
        if not (elem in elems):
            elems.add(elem)
            yield elem



# numbers = [1, 2, 2, 3, 4, 5, 5, 5]

# print(*unique(numbers))

iterator = iter('111222333')
uniques = unique(iterator)

print(next(uniques))
print(next(uniques))
print(next(uniques))
