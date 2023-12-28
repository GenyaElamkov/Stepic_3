"""
Функция pairwise()
Реализуйте генераторную функцию, которая принимает один аргумент:

iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной элемент итерируемого объекта iterable, а также следующий за ним элемент:

(<очередной элемент>, <следующий элемент>)
Для последнего элемента следующим считается значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.

https://stepik.org/lesson/673155/step/21?unit=671418
"""


# def pairwise(iterable):
#     if not iterable:
#         return iterable

#     for i, elem in enumerate(iterable):
#         if i == 0:
#             tmp = elem
#             continue
#         yield tmp, elem
#         tmp = elem
#     yield tmp, None


def pairwise(iterable):
    it = iter(iterable)
    i = next(it, None)
    while i is not None:
        i, prev = next(it, None), i
        yield prev, i


numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))


# iterator = iter('stepik')

# print(*pairwise(iterator))

# print(list(pairwise([])))
