"""
Добавляет в каждый JSON-объект из данного списка все недостающие ключи,
присваивая этим ключам значение null. Ключ считается недостающим,
если он присутствует в каком-либо другом объекте, но отсутствует в данном.
Программа должна создать список с обновленными JSON-объектами и записать
его в файл updated_people.json.

https://stepik.org/lesson/623073/step/9?unit=618703
"""
import json

with (
    open("../files/people.json", "r", encoding="utf-8") as f,
    open("../files/updated_people.json", "w", encoding="utf-8") as out_f,
):
    data = json.load(f)

    arr_key = sorted(set([k for dic in data for k in dic.keys()]))

    all_dic = []
    for dic in data:
        tmp = {}
        for k in arr_key:
            tmp[k] = None
            if k in dic:
                tmp[k] = dic[k]

        all_dic.append(tmp)

    json.dump(all_dic, out_f, indent=3)
