"""
Вам доступен именованный кортеж Student, который содержит данные об ученике. Первым элементом именованного кортежа является фамилия ученика, вторым — имя, третьим — класс. Также доступен список students, содержащий эти кортежи.

Дополните приведенный ниже код, чтобы он вывел наиболее часто встречаемое имя среди учеников из данного списка.

https://stepik.org/lesson/674263/step/16?unit=672698
"""

from collections import namedtuple
from itertools import groupby

Student = namedtuple('Student', ['surname', 'name', 'grade'])

students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
            Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
            Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
            Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
            Student('Елькина', 'Мария', 11),Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
            Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
            Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
            Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
            Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]



res = groupby(sorted(students, key=lambda n: n.name), key=lambda x: x.name)

often_names = []
for k, values in res:
    counter_name = len([val.name for val in values])
    often_names.append((k, counter_name))

print(max(often_names, key=lambda x: x[1])[0])

if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
