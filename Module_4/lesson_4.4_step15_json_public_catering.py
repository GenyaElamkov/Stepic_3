"""
Напишите программу, которая:

определяет район Москвы, в котором находится больше всего заведений,
и выводит название этого района и количество заведений в нем
определяет сеть с самым большим числом заведений и выводит название этой
сети и количество заведений этой сети
Полученные значения программа должна вывести в следующем формате:

<район>: <количество заведений>
<название сети>: <количество заведений>

https://stepik.org/lesson/623073/step/15?unit=618703
"""
import json

with open("food_services.json", "r", encoding="utf-8") as file_json:
    src = json.load(file_json)
    district = {}
    operating_company = {}
    for dic in src:
        district[dic["District"]] = district.get(dic["District"], 0) + 1
        operating_company[dic["OperatingCompany"]] = operating_company.get(dic["OperatingCompany"], 0) + 1

del operating_company['']
print(f"{max(district, key=district.get)}: {max(district.values())}")
print(f"{max(operating_company, key=operating_company.get)}: {max(operating_company.values())}")
