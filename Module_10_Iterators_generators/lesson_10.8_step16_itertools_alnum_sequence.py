"""
Функция alnum_sequence()
Реализуйте функцию alnum_sequence(), которая не принимает никаких аргументов.

Функция должна возвращать итератор, циклично генерирующий бесконечную последовательность натуральных чисел и заглавных латинских букв:

1,A,2,B,3,C,..,X,25,Y,26,Z

https://stepik.org/lesson/640045/step/16?unit=636565
"""

import itertools
import string


def alnum_sequence():
    """
    >>> alnum = alnum_sequence()
    >>> print(*(next(alnum) for _ in range(55)))
    1 A 2 B 3 C 4 D 5 E 6 F 7 G 8 H 9 I 10 J 11 K 12 L 13 M 14 N 15 O 16 P 17 Q 18 R 19 S 20 T 21 U 22 V 23 W 24 X 25 Y 26 Z 1 A 2
    """
    iterable = zip(range(1, len(string.ascii_uppercase) + 1), string.ascii_uppercase)
    return itertools.cycle(elem for elems in iterable for elem in elems)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
