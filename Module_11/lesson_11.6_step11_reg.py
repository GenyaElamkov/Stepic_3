"""
Одинаковые слоги
Напишите программу, которая выводит слова, состоящие из двух одинаковых слогов.

Формат входных данных
На вход программе подается произвольное количество слов, каждое на отдельной строке.

Формат выходных данных
Программа должна из введенных слов вывести только те, которые состоят из двух одинаковых слогов. Слова должны быть расположены в своем исходном порядке, каждое на отдельной строке.

https://stepik.org/lesson/640164/step/6?unit=636683
"""

import re
import sys

pattern = r"b(.*)\1\b"

for text in sys.stdin.read().splitlines():
    match = re.fullmatch(pattern, text)
    print(match)
    

    
