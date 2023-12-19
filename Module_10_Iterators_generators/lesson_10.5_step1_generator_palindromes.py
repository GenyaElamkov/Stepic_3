"""
Функция palindromes()
Реализуйте генераторную функцию palindromes(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий бесконечную последовательность натуральных чисел-палиндромов.

Примечание 1. Число-палиндром — число, которое читается одинаково как справа налево, так и слева направо.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию palindromes(), но не код, вызывающий ее.


https://stepik.org/lesson/640048/step/26?thread=solutions&unit=636568
"""

from typing import Any, Generator


def palindromes() -> Generator[int, Any, None]:
    counter = 0
    while True:
        counter += 1
        if str(counter) == str(counter)[::-1]:
            yield counter


generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)
