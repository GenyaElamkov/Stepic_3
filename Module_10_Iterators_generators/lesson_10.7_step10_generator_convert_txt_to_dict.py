"""
Функция txt_to_dict()
Вам доступен файл planets.txt, содержащий информацию о различных планетах. В первых четырех строках указаны характеристики первой планеты, после чего следует пустая строка, затем характеристики второй планеты, и так далее:

Name = Mercury
Diameter = 4879.4
Mass = 3.302×10^23
OrbitalPeriod = 0.241

Name = Venus
Diameter = 12103.6
Mass = 4.869×10^24
OrbitalPeriod = 0.615

...
Реализуйте генераторную функцию txt_to_dict(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий последовательность словарей, каждый из которых содержит информацию об очередной планете из файла planets.txt, а именно ее название, диаметр, массу и орбитальный период. Например:

{'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}

https://stepik.org/lesson/673155/step/11?unit=671418
"""


from typing import Any, Generator


def txt_to_dict() -> Generator[dict, Any, None]:
    with open(
        r"D:\python_2022\Stepic_3\Stepic_3\Module_10_Iterators_generators\planets.txt",
        "r",
        encoding="utf-8",
    ) as file:
        d = {}
        for line in file:
            line = line.strip("\n")
            if line != "":
                d.setdefault(*line.split(" = "))
            else:
                yield d
                d = {}
        yield d


planets = txt_to_dict()
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))

# txt_to_dict()
