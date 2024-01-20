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

pattern_findall = r"(bee).*\1"
pattern_search = r"\b(geek)\b"

cnt_bee = 0
cnt_geek = 0
for text in sys.stdin.read().splitlines():
    match_1 = re.search(pattern_search, text)
    match_2 = re.findall(pattern_findall, text)
    if match_2: cnt_bee += 1
    if match_1: cnt_geek += 1
print(cnt_bee, cnt_geek, sep='\n')
    
