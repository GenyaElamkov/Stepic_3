"""
Вычисляет контрольную сумму для объекта, содержащегося в pickle файле,
и сравнивает ее с данным целым числом.

https://stepik.org/lesson/584474/step/15?unit=579234
"""
import pickle

# date = ["eqe", "w", "a", 45.9]
# date = [1, 2, 3, "eqe", "w", 10, "a", 45.9]
# date = {1: "safa", 2: "eqe", "w": 10, 12.4: "sfsdf"}
# date = {"safa": "safa", "eqe": "eqe", "w": 10, 12.4: "sfsdf"}
date = ['a', 'c', 'c', [1, 2, '3'], 'f', (1, 2, 4, 5, 7), {'a', 'f', 'h', 1}]
with open(input(), "rb") as file:
    date = pickle.load(file)

num = list(filter(lambda x: isinstance(x, int), date))
res = ''
if isinstance(date, dict):
    res = sum(num)
elif isinstance(date, list):
    res = min(num, default=0) * max(num, default=0)

if int(input()) == res:
    print("Контрольные суммы совпадают")
else:
    print("Контрольные суммы не совпадают")
