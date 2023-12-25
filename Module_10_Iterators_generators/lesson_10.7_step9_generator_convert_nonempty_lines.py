"""
Функция nonempty_lines()
Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:

file — название текстового файла, например, data.txt
Функция должна возвращать генератор, порождающий последовательность всех непустых строк файла file с убранным символом переноса строки \n. Если строка содержит более 
25
25 символов, она заменяется многоточием ....

Примечание 1. При открытии файла используйте явное указание кодировки UTF-8.

https://stepik.org/lesson/673155/step/9?unit=671418
"""


from typing import Any, Generator


def nonempty_lines(file: str) -> Generator[str, Any, None]:
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            text = line.strip("\n")
            if not text:
                continue
            if len(text) > 25:
                text = "..."
            yield text


file_name = "Module_10_Iterators_generators\\file1.txt"
lines = nonempty_lines(file_name)
# print(lines)

print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))
