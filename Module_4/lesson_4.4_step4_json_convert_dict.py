"""
Ниже представлена программа, которая должна преобразовать словарь
specs в строку в формате JSON и вывести ее с отступами в три пробела,
не заменяя кириллические символы на их коды.

https://stepik.org/lesson/623073/step/4?unit=618703
"""

import json

specs = {
    "Модель": "AMD Ryzen 5 5600G",
    "Год релиза": 2021,
    "Сокет": "AM4",
    "Техпроцесс": "7 нм",
    "Ядро": "Cezanne",
    "Объем кэша L2": "3 МБ",
    "Объем кэша L3": "16 МБ",
    "Базовая частота": "3900 МГц",
}


specs_json = json.dumps(specs, ensure_ascii=False, indent=3)

print(specs_json)
