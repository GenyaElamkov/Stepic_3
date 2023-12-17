"""
Функция alternating_sequence()
Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:

count — натуральное число, по умолчанию имеет значение None
Если count имеет значение None, функция должна возвращать генератор, порождающий бесконечный знакочередующийся ряд натуральных чисел.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий первые count чисел знакочередующегося ряда натуральных чисел, а затем возбуждающий исключение StopIteration.

Примечание 1. Знакочередующийся ряд натуральных чисел имеет вид:

1,−2,3,−4,5,−6,7,−8,9,−10,...
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую генераторную  функцию alternating_sequence(), но не код, вызывающий ее.

https://stepik.org/lesson/640048/step/16?unit=636568
"""


from typing import Any, Generator


def alternating_sequence(count: int | None = None) -> Generator[int, Any, None]:
    counter = 0
    while counter != count:
        counter += 1
        yield (-counter, counter)[counter % 2]


generator = alternating_sequence()

print(next(generator))
print(next(generator))


# generator = alternating_sequence(10)

# print(*generator)
