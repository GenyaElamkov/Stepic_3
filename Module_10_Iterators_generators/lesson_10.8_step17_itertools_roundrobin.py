"""
Функция roundrobin() 🌶️
Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом.

Функция должна возвращать итератор, генерирующий последовательность из элементов всех переданных итерируемых объектов: сначала первый элемент первого итерируемого объекта, затем первый элемент второго итерируемого объекта, и так далее; после второй элемент первого итерируемого объекта, затем второй элемент второго итерируемого объекта, и так далее.

Примечание 1. Элементы итерируемых объектов в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

https://stepik.org/lesson/640045/step/16?unit=636565
"""


import itertools


def roundrobin(*args):
    """
    >>> print(*roundrobin('abc', 'd', 'ef'))
    a d e b f c
    >>> numbers = [1, 2, 3]
    >>> letters = iter('beegeek')
    >>> print(*roundrobin(numbers, letters))
    1 b 2 e 3 e g e e k
    >>> print(list(roundrobin()))
    []
    >>> numbers = iter([1, 2, 3])
    >>> nones = iter([None, None, None, None])
    >>> print(*roundrobin(numbers, nones))
    1 None 2 None 3 None None
    """
    return (
        elem
        for elems in itertools.zip_longest(*args, fillvalue = '')
        for elem in elems
        if elem != ''
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
