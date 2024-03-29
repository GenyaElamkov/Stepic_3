"""
Объединил данные словари в список и записал полученную структуру данных
в файл data.json, указав в качестве отступов три символа пробела.

https://stepik.org/lesson/623073/step/3?unit=618703
"""

import json

club1 = {
    "name": "FC Byern Munchen",
    "country": "Germany",
    "founded": 1900,
    "trainer": "Julian Nagelsmann",
    "goalkeeper": "M. Neuer",
    "league_position": 1,
}

club2 = {
    "name": "FC Barcelona",
    "country": "Spain",
    "founded": 1899,
    "trainer": "Xavier Creus",
    "goalkeeper": "M. Ter Stegen",
    "league_position": 7,
}

club3 = {
    "name": "FC Manchester United",
    "country": "England",
    "founded": 1878,
    "trainer": "Michael Carrick",
    "goalkeeper": "D. De Gea",
    "league_position": 8,
}

clubs = [club1, club2, club3]

with open("../files/data.json", "w", encoding="utf-8") as f:
    json.dump(clubs, f, indent=3)
