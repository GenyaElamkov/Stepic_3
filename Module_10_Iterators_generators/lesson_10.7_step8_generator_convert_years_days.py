"""
Функция years_days()
Реализуйте генераторную функцию years_days(), которая принимает один аргумент:

year — натуральное число
Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.

Примечание 1. Возьмем в качестве примера 
2022 год. В январе этого года 31
31 день, в феврале — 
28, в марте — 
31, и так далее. Тогда генератор, полученный при вызове years_days(2022), должен порождать сначала все даты с 
1 по 
31 января, затем с 
1 по 
28 февраля, и так далее до 
31 декабря.

https://stepik.org/lesson/673155/step/9?unit=671418
"""


import datetime
from typing import Any, Generator

def years_days(year: int) -> Generator[str, Any, None]:
    start_date = datetime.datetime(year, month=1, day=1)
    end_date = datetime.datetime(year, month=12, day=31)
    while start_date <= end_date:
        yield start_date.strftime("%Y-%m-%d")
        start_date += datetime.timedelta(days=1)
        

dates = years_days(2077)

print(*dates)