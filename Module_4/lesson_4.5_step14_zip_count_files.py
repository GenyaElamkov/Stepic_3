"""
Программа, которая выводит единственное число — количество файлов
в этом архиве.

https://stepik.org/lesson/547172/step/14?unit=540798
"""

from zipfile import ZipFile

with ZipFile("./files/workbook.zip") as zip_file:
    # res = sum(True for dir in info if dir.is_dir() == False)
    res = len(list(filter(lambda x: not x.is_dir(), zip_file.infolist())))
print(res)
