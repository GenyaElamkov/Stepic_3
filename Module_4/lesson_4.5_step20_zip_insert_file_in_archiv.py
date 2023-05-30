"""
Добавил в архив files.zip только те файлы из списка file_names, объем
которых не превышает 100 байт.

https://stepik.org/lesson/547172/step/20?unit=540798
"""

import os.path
from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf',
              'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py',
              'test.py']

with ZipFile("files.zip", mode="a") as zip_file:
    for file_name in file_names:
        if os.path.getsize(file_name) < 100:
            zip_file.write(file_name)

# print(type(os.path.getsize("lesson_4.5_step19_zip_setup_archivpy.py")))
