"""
Функция palindromes()
Реализуйте генераторную функцию palindromes(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий бесконечную последовательность натуральных чисел-палиндромов.

Примечание 1. Число-палиндром — число, которое читается одинаково как справа налево, так и слева направо.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию palindromes(), но не код, вызывающий ее.


https://stepik.org/lesson/640048/step/26?thread=solutions&unit=636568
"""

from typing import Any, Generator



def flatten(nested_list: int | list[int]) -> Generator[int, Any, None]:
    for num in nested_list:
        if isinstance(num, int):
            yield num
        else:
            yield from flatten(num)



generator = flatten([1, 2, 3, 4, 5, 6, 7])
print(*generator)

# generator = flatten([[1, 2], [[3]], [[4], 5]])
# print(*generator)