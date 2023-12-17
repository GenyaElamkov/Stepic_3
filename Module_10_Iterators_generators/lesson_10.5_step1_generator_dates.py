"""
Функция dates()
Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:

start — дата, тип date
count — натуральное число, по умолчанию имеет значение None
Если count имеет значение None, функция должна возвращать генератор, порождающий последовательность из максимально допустимого количества дат (тип date), начиная с даты start.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий последовательность из count дат (тип date), начиная с даты start, а затем возбуждающий исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию dates(), но не код, вызывающий ее.

https://stepik.org/lesson/640048/step/19?unit=636568
"""

from datetime import date, timedelta
from typing import Any, Generator


def dates(start: date, count: int | None = None) -> Generator[date, Any, None]:
    counter = 0
    while count != counter:
        try:
            yield start + timedelta(days=counter)
            counter += 1
        except OverflowError:
            break



# generator = dates(date(2022, 3, 8))

# print(next(generator))
# print(next(generator))
# print(next(generator))

# generator = dates(date(2022, 3, 8), 5)

# print(*generator)

generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print("Error")
