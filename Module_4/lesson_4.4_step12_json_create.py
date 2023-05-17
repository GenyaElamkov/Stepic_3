"""
Создать файл data.csv с двумя столбцами — name (имя) и phone (номер),
и записать в него данные выбранных студентов, расположив их в
лексикографическом порядке имён. В качестве разделителя в файле data.csv
должна быть использована запятая.

https://stepik.org/lesson/623073/step/12?unit=618703
"""
import csv
import json

with (
    open("students.json", "r", encoding="utf-8") as json_file,
    open("data.csv", "w", encoding="utf-8", newline="") as csv_file,
):
    src = json.load(json_file)
    header = ["name", "phone"]
    arr = []
    for dic in src:
        if dic["age"] >= 18 and dic["progress"] >= 75:
            arr.append([dic["name"], dic["phone"]])

    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(header)
    writer.writerows(sorted(arr))
