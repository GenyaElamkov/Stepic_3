"""
Функция parse_ranges()
Назовем диапазоном запись двух натуральных чисел через дефис a-b, где a — левая граница диапазона, b — правая граница диапазона, причем a <= b. Диапазон содержит в себе все числа от a до b включительно. Например, диапазон 1-4 содержит числа 

Реализуйте генераторную функцию parse_ranges(), которая принимает один аргумент:

ranges — строка, в которой через запятую указаны диапазоны чисел
Функция должна возвращать генератор, порождающий последовательность чисел, содержащихся в диапазонах ranges.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию parse_ranges(), но не код, вызывающий ее.

https://stepik.org/lesson/673155/step/6?unit=671418
"""


from typing import Generator


# def parse_ranges(ranges: str) -> Generator[int, None, None]:
#     nums = (num.split("-") for num in ranges.split(","))
#     res = (range(int(num[0]), int(num[1]) + 1) for num in nums)
#     return (nm for num in res for nm in num)



def parse_ranges(ranges: str):
    for r in ranges.split(","):
        start, end = map(int, r.split("-"))
        yield from range(start, end+1)

print(*parse_ranges("7-32"))

