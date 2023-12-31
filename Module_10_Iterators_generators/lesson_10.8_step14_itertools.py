"""
Функция tabulate()
Реализуйте функцию tabulate(), которая принимает один аргумент:

func — произвольная функция
Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность возвращаемых значений функции func сначала с аргументом 1, затем 2, затем 3, и так далее.


https://stepik.org/lesson/640045/step/15?unit=636565
"""

from itertools import count, starmap


def tabulate(func):
    """
    >>> func = lambda x: x + 10
    >>> values = tabulate(func)
    >>> print(next(values))
    11
    >>> print(next(values))
    12
    >>> print(next(values))
    13
    """
    return (func(num) for num in count(1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
