"""
Программа, которая определяет бассейн, подходящий Тимуру.
Программа должна вывести его размеры и адрес в следующем формате:

<длина>x<ширина>
<адрес>

https://stepik.org/lesson/623073/step/13?unit=618703
"""

import json
from datetime import datetime

pattern = "%H:%M"
start_time = datetime.strptime("10:00", pattern).time()
finsh_time = datetime.strptime("12:00", pattern).time()

with open("files/pools.json", "r", encoding="utf-8") as file:
    src = json.load(file)
    length_max = 0
    width_max = 0
    for dic in src:
        dt = dic["WorkingHoursSummer"]["Понедельник"].split("-")
        dt_start = datetime.strptime(dt[0], pattern).time()
        dt_fish = datetime.strptime(dt[1], pattern).time()

        if start_time >= dt_start and finsh_time <= dt_fish:
            length = dic['DimensionsSummer']['Length']
            width = dic['DimensionsSummer']['Width']
            if length > length_max and width >= width_max:
                length_max = length
                width_max = width
                dimension = f"{length_max}x{width_max}"
                address = dic["Address"]
    else:
        print(dimension, address, sep="\n")


# def best_pool(data: dict):
#     monday_time = data["WorkingHoursSummer"]["Понедельник"].split("-")
#     start, finish = [int(time.split(":")[0]) for time in monday_time]
#     time = True if start <= 10 and finish >= 12 else False
#     dimensions = data["DimensionsSummer"]
#
#     return (time, dimensions["Length"], dimensions["Width"])
#
# with open("pools.json", "r", encoding="utf-8") as input_file:
#     input_data = json.load(input_file)
#
#     choice = max(input_data, key=best_pool)
#     print(f'{choice["DimensionsSummer"]["Length"]}x{choice["DimensionsSummer"]["Width"]}')
#     print(choice["Address"])