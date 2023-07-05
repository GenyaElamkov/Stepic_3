from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "height"])

ExtendedPerson = namedtuple("ExtendedPerson", [*Person._fields, "country"],
                            defaults=['Russian', ])

timur = ExtendedPerson("Тимур", 29, 170, 65)
# print(ExtendedPerson._fields)
# print(timur._fields)

# for field, value in zip(Person._fields, timur):
#     print(field, '->', value)
#
# print(timur)
# print(timur._field_defaults)
# print(Person._field_defaults)


# Метод _make()
Person = namedtuple("Person", ["name", "age", "height"])
timur = Person._make(['Timur', 29, 170])

# print(timur._asdict())
# print(type(timur._asdict()))

# timur_2 = timur._replace(age=30, height=180)
timur._replace(age=30, height=180)
print(timur._asdict())
# print(timur_2._asdict())
print(timur.height)

Game = namedtuple('Game', 'name developer publisher')

ExtendedGame = namedtuple('ExtendedGame',
                          [*Game._fields, 'release_date', 'price'])

print(ExtendedGame)
