"""
Вам доступен именованный кортеж Animal, который содержит данные о животном.
 Первым элементом именованного кортежа является имя животного,
 вторым — семейство, третьим — пол, четвертым — цвет.
 Также доступен файл data.pkl, содержащий сериализованный список таких кортежей.

Дополните приведенный ниже код, чтобы для каждого кортежа из этого
списка он вывел названия его полей и значения этих полей в следующем формате:

name: <значение>
family: <значение>
sex: <значение>
color: <значение>


https://stepik.org/lesson/740203/step/10?unit=741843
"""

import pickle
from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    for animal in pickle.load(file):
        print(f"name: {animal.name}\n"
              f"family: {animal.family}\n"
              f"sex: {animal.sex}\n"
              f"color: {animal.color}\n")
