"""
Объединяет два данных JSON-объекта в один JSON-объект, причем если
пары из первого и второго объектов имеют совпадающие ключи, то значение
следует взять из второго объекта. Полученный JSON-объект программа
должна записать в файл data_merge.json

https://stepik.org/lesson/623073/step/8?unit=618703
"""

import json

filename_1 = "../files/data1.json"
filename_2 = "../files/data2.json"
filename_out = "../files/data_merge.json"
with (
    open(filename_1, "r", encoding="utf-8") as f1,
    open(filename_2, "r", encoding="utf-8") as f2,
    open(filename_out, "w", encoding="utf-8") as out_file,
):
    data_1, data_2 = json.load(f1), json.load(f2)
    data_1.update(data_2)

    json.dump(data_1, out_file, indent=3)

    # Вариант решения
    # json.dump(data1 | data2, outer)
