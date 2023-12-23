"""
Вам доступен именованный кортеж Person, который содержит данные о человеке. Первым элементом именованного кортежа является имя и фамилия человека, вторым — национальность, третьим — пол, четвертым — год рождения, пятым — год смерти. Если человек жив, год смерти считается равным 
0
0. Также доступен список persons, содержащий эти кортежи.

Дополните приведенный ниже код с использованием конвейеров генераторов, чтобы он вывел имя и фамилию самого молодого живого мужчины (male) из Швеции (Swedish).

https://stepik.org/lesson/673155/step/5?unit=671418
"""

from collections import namedtuple

Person = namedtuple("Person", ["name", "nationality", "sex", "birth", "death"])

persons = [
    Person("E. M. Ashe", "American", "male", 1867, 1941),
    Person("Goran Aslin", "Swedish", "male", 1980, 0),
    Person("Erik Gunnar Asplund", "Swedish", "male", 1885, 1940),
    Person("Genevieve Asse", "French", "female", 1949, 0),
    Person("Irene Adler", "Swedish", "female", 2005, 0),
    Person("Sergio Asti", "Italian", "male", 1926, 0),
    Person("Olof Backman", "Swedish", "male", 1999, 0),
    Person("Alyson Hannigan", "Swedish", "female", 1940, 1987),
    Person("Dana Atchley", "American", "female", 1941, 2000),
    Person("Monika Andersson", "Swedish", "female", 1957, 0),
    Person("Shura_Stone", "Russian", "male", 2000, 0),
    Person("Jon Bale", "Swedish", "male", 2000, 0),
]

# live = filter(
#     lambda x: x.nationality == "Swedish" and x.death == 0 and x.sex == "male", persons
# )
# young = max(live, key=lambda x: x.birth)

sex_male = (person for person in persons if person.sex == "male")
lives = (person for person in sex_male if person.death == 0)
sitys = (sity for sity in lives if sity.nationality == "Swedish")
young = max(sitys, key=lambda x: x.birth)

print(young.name)