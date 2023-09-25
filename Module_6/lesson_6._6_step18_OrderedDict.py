"""
Вам доступен словарь data с четным количеством элементов.
Дополните приведенный ниже код, чтобы он вывел данный словарь, расположив
его элементы по следующему правилу: первый, последний, второй, предпоследний,
третий, и так далее.

https://stepik.org/lesson/634520/step/18?unit=630783
"""

from collections import OrderedDict

data = OrderedDict(
    {'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
     'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
     'District': 'район Арбат',
     'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
     'SeatsCount': '10'})

# new_data = OrderedDict()
# for rule in map(lambda x: x % 2, list(range(len(data)))):
#     k, v = data.popitem(rule)
#     new_data[k] = v
# print(new_data)

# new_data = OrderedDict(data.popitem(rule) for rule in map(lambda x: x % 2, list(range(len(data)))))
# print(new_data)

data = OrderedDict([data.popitem(last=i % 2) for i in range(len(data))])

print(data)
