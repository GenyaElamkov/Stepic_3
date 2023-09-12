"""
Вам доступен словарь data. Дополните приведенный ниже код, чтобы он вывел
данный словарь, расположив его элементы в обратном порядке.


https://stepik.org/lesson/634520/step/17?unit=630783
"""

from collections import OrderedDict

data = OrderedDict(
    {'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
     'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ',
     'District': 'район Арбат',
     'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
     'SeatsCount': '10'})


# for k in reversed(list(data)):
#     data.move_to_end(k)
#
# print(data)

print(OrderedDict(reversed(data.items())))