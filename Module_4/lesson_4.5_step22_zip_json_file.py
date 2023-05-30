"""
Обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов,
 выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены
 в лексикографическом порядке имен, а при совпадении — в лексикографическом
 порядке фамилий, каждый на отдельной строке.

https://stepik.org/lesson/547172/step/22?unit=540798
"""

import json
from zipfile import ZipFile


def is_correct_json(string: str) -> bool:
    try:
        return bool(json.loads(string))
    except json.decoder.JSONDecodeError:
        return False



with ZipFile("data.zip") as zip_file:
    info = zip_file.infolist()
    for file in info:
        if not file.is_dir():
            w