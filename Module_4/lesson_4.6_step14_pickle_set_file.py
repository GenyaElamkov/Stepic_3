"""
Создавать pickle файл с названием filename, который содержит сериализованный
список только тех объектов из списка objects, тип которых равен typename

https://stepik.org/lesson/584474/step/14?unit=579234
"""

import pickle


def filter_dump(filename, objects, typename):
    obj = list(filter(lambda x: isinstance(x, typename), objects))
    with open(filename, "wb") as file:
        pickle.dump(obj, file)


if __name__ == "__main__":
    filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
