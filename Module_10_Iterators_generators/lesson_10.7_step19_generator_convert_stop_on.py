"""
Функция stop_on()
Реализуйте генераторную функцию, которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
obj — произвольный объект
Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable до тех пор, пока не будет достигнут элемент, равный obj. Если итерируемый объект iterable не содержит ни одного элемента, равного obj, генератор должен породить все элементы iterable.

https://stepik.org/lesson/673155/step/20?unit=671418
"""


def stop_on(iterable, obj):
    for elem in iterable:
        if elem == obj:
            break
        yield elem

# numbers = [1, 2, 3, 4, 5]

# print(*stop_on(numbers, 4))
        
iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))