"""
Перестановки
Напишите программу, которая выводит все перестановки символов строки без дубликатов.

Формат входных данных
На вход программе подается произвольная строка из строчных латинских букв, длина которой не превышает 
10 символов.

Формат выходных данных
Программа должна вывести все перестановки символов данной строки без дубликатов в алфавитном порядке, каждую на отдельной строке.

https://stepik.org/lesson/674263/step/16?unit=672698

"""

from itertools import permutations

for chars in sorted(set(permutations(input()))):
    print(''.join(chars))


if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
