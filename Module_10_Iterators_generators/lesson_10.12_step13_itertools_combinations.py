"""
Задача о рюкзаке
Вам доступен список items, содержащий набор предметов. Каждый предмет представлен в виде именованного кортежа и имеет три параметра — название, массу (в граммах) и ценность (в рублях). Также имеется рюкзак определённой грузоподъёмности.

Напишите программу, которая определяет, какие предметы из представленного набора следует взять, чтобы собрать рюкзак с максимальной ценностью предметов внутри, соблюдая при этом весовое ограничение рюкзака.

Формат входных данных
На вход программе в первой строке подается число — грузоподъемность рюкзака (в граммах).

Формат выходных данных
Программа должна определить какие предметы из представленного набора следует взять, чтобы собрать рюкзак с максимальной ценностью предметов внутри, соблюдая при этом весовое ограничение рюкзака, и вывести названия полученных предметов в лексикографическом порядке, каждое на отдельной строке. Если рюкзак не позволяет взять ни один предмет, программа должна вывести текст:

Рюкзак собрать не удастся
Примечание 1. Рюкзак не обязательно должен быть наполнен полностью.

https://stepik.org/lesson/674263/step/16?unit=672698
"""

from collections import namedtuple
import itertools

Item = namedtuple("Item", ["name", "mass", "price"])

items = [
    Item("Обручальное кольцо", 7, 49_000),
    Item("Мобильный телефон", 200, 110_000),
    Item("Ноутбук", 2000, 150_000),
    Item("Ручка Паркер", 20, 37_000),
    Item("Статуэтка Оскар", 4000, 28_000),
    Item("Наушники", 150, 11_000),
    Item("Гитара", 1500, 32_000),
    Item("Золотая монета", 8, 140_000),
    Item("Фотоаппарат", 720, 79_000),
    Item("Лимитированные кроссовки", 300, 80_000),
]

# start_massa = int(input())
start_massa = 9000
max_price = 0
result = ""
for i in range(1, len(items) + 1):
    for k in list(itertools.combinations(items, i)):
        massa = sum(val.mass for val in k)
        if massa <= start_massa:
            price = sum(val.price for val in k)
            if max_price <= price:
                max_price = price
                result = [val.name for val in k]
if not result:
    print("Рюкзак собрать не удастся")
print(*sorted(result), sep="\n")


if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
