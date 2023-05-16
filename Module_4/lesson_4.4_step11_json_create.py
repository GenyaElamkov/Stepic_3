"""
Создающую JSON-объект, ключом в котором является административный округ,
а значением — JSON-объект, в котором, в свою очередь, ключом является название
района, относящийся к этому административному округу, а значением — список
адресов всех площадок в этом районе. Полученный JSON-объект программа должна
записать в файл addresses.json.

https://stepik.org/lesson/623073/step/11?unit=618703
"""

import csv
import json

with (open("playgrounds.csv", "r", encoding="utf-8") as f,
      open("addresses.json", "w", encoding="utf-8") as out_file):

    reader = csv.DictReader(f, delimiter=";")
    district = {}
    for dic in reader:
        district.setdefault(dic["AdmArea"], {}).setdefault(dic["District"],
                                                    []).append(dic["Address"])

    json.dump(district, out_file, indent=3, ensure_ascii=False)
