"""
Обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов,
 выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены
 в лексикографическом порядке имен, а при совпадении — в лексикографическом
 порядке фамилий, каждый на отдельной строке.

https://stepik.org/lesson/547172/step/22?unit=540798
"""

import json
from zipfile import ZipFile


def is_correct_json(file_json) -> list | bool:
    team = "Arsenal"
    try:
        string = json.dumps(json.load(file_json))
        src = json.loads(string)
        if src["team"] == team:
            return [src["first_name"], src["last_name"]]
    except json.decoder.JSONDecodeError:
        return False
    except UnicodeDecodeError:
        return False


result = []
with ZipFile("data.zip") as zip_file:
    for file in zip_file.infolist():
        if file.is_dir():
            continue
        if not file.filename.endswith(".json"):
            continue
        zip_file.extract(file.filename)

        with open(file.filename, "r", encoding="utf-8") as file_json:
            json_player = is_correct_json(file_json)
            if json_player:
                result.append(json_player)

for item in sorted(sorted(result, key=lambda x: x[1])):
    print(*item)
