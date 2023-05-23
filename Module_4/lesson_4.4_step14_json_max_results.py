"""
Программа, которая для каждого студента определяет его максимальную оценку,
а также дату и время ее получения. Программа должна создать список словарей,
каждый из которых содержит следующие пары ключ-значение:

name — имя студента
surname — фамилия студента
best_score — максимальная оценка за экзамен
date_and_time — дата и время получения максимальной оценки в исходном формате
email — адрес электронной почты
Полученный список программа должна записать в файл best_scores.json, причем
словари в списке должны быть расположены в лексикографическом порядке названий
электронных почт.

https://stepik.org/lesson/623073/step/14?unit=618703
"""

import csv
import json
from datetime import datetime

pattern = "%Y-%m-%d %H:%M:%S"

with (open("exam_results.csv", "r", encoding="utf-8") as file_csv,
      open("best_scores.json", "w", encoding="utf-8") as file_json):
    src = csv.DictReader(file_csv, delimiter=",")

    students = {}
    for dic in src:
        students.setdefault(dic["email"], {}).setdefault("name", dic["name"])
        students.setdefault(dic["email"], {}).setdefault("surname",
                                                         dic["surname"])
        students.setdefault(dic["email"], {}).setdefault("best_score",
                                                         int(dic["score"]))

        date = datetime.strptime(dic["date_and_time"], pattern)
        students.setdefault(dic["email"], {}).setdefault("date_and_time", date)

        score = int(dic["score"])
        if (students[dic["email"]]["best_score"] <= score and
                students[dic["email"]]["date_and_time"] < date):
            students[dic["email"]]["best_score"] = score
            students[dic["email"]]["date_and_time"] = date

    arr_json = []
    for k, v in sorted(students.items()):
        v["date_and_time"] = v["date_and_time"].strftime(pattern)
        v["email"] = v.setdefault("email", k)
        arr_json.append(v)
    json.dump(arr_json, file_json, indent=3)
