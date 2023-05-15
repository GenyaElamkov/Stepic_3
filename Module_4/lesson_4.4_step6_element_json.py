"""
Принимает на вход описание одного объекта в формате JSON и выводит
все пары ключ-значение этого объекта.

https://stepik.org/lesson/623073/step/6?unit=618703
"""

import json
import timeit
from sys import stdin

# start = timeit.timeit()
for k, v in json.loads(stdin.read()).items():
    if isinstance(v, list):
        print(f"{k}: {', '.join(map(str, v))}")
    else:
        print(f"{k}: {v}")
finish = timeit.timeit()

print(finish)
