"""
Cоздает единственный JSON-объект, имеющий в качестве ключа название религии,
а в качестве значения — список стран, в которых исповедуется данная религия.
Полученный JSON-объект программа должна записать в файл religion.json

https://stepik.org/lesson/623073/step/10?unit=618703
"""

import json

with (
    open("../files/countries.json", "r", encoding="utf-8") as f,
    open("../files/religion.json", "w", encoding="utf-8") as out_file,
):
    data = json.load(f)
    all_region = {}
    for dic in data:
        all_region[dic["religion"]] = all_region.setdefault(dic["religion"],
                                                        []) + [dic["country"]]

    json.dump(all_region, out_file, indent=3)
