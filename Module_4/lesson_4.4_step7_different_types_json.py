"""
создает список, элементами которого являются объекты из списка, содержащегося
в файле data.json, измененные по следующим правилам:

если объект является строкой, в его конец добавляется восклицательный знак
если объект является числом, он увеличивается на единицу
если объект является логическое значением, он инвертируется
если объект является списком, он удваивается
если объект является JSON-объектом (словарем), в него добавляется новая пара
 "newkey": null
если объект является пустым значением (null), он не добавляется

https://stepik.org/lesson/623073/step/7?unit=618703
"""

import json

with (
    open("../files/data.json", "r", encoding="utf-8") as f,
    open("../files/updated_data.json", "w", encoding="utf-8") as out_file,
):
    data = json.load(f)
    arr = []
    for key in data:
        if isinstance(key, str):
            arr.append(key + "!")
        elif isinstance(key, bool):
            arr.append(not key)
        elif isinstance(key, int):
            arr.append(key + 1)
        elif isinstance(key, list):
            arr.append(key * 2)
        elif isinstance(key, dict):
            key["newkey"] = None
            arr.append(key)
        elif not key:
            continue
    json.dump(arr, out_file, indent=3)

# Вариант решения
# opers = {str: lambda x: x + '!',
#          int: lambda x: x + 1,
#          float: lambda x: x + 1,
#          bool: lambda x: not x,
#          list: lambda x: x * 2,
#          dict: lambda x: x | {'newkey': None}}
#
# with open('data.json', encoding='utf8') as fi, open('updated_data.json', 'w', encoding='utf8') as fo:
#     json.dump([opers[type(i)](i) for i in json.load(fi) if type(i) in opers], fo, indent=3)
