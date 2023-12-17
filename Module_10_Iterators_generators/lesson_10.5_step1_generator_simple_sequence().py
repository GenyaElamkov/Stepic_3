"""
Функция simple_sequence()
Реализуйте генераторную функцию simple_sequence(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий бесконечную возрастающую последовательность натуральных чисел, в которой каждое число встречается столько раз, каково оно:
1,2,2,3,3,3,4,4,4,4,..
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию simple_sequence(), но не код, вызывающий ее.

https://stepik.org/lesson/640048/step/15?unit=636568

"""


from typing import Any, Generator


def simple_sequence() -> Generator[int, Any, None]:
    counter = 1
    while True:
        for _ in range(counter):
            yield counter
        counter += 1

generator = simple_sequence()

for _ in range(10):
    print(next(generator))
