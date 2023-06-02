"""
Вызывает данную функцию с заданными аргументами и выводит возвращаемое
значение функции.

https://stepik.org/lesson/584474/step/13?unit=579234
"""

import pickle
import sys

with open(input(), "rb") as file:
    func_test = pickle.load(file)

print(func_test(*list(map(str.strip, sys.stdin))))
