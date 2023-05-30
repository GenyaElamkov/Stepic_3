"""
Модуль zipfile. Help.

https://stepik.org/lesson/547172/step/1?unit=540798
"""

from zipfile import ZipFile

# Работа с zip файлами в Python.

# with ZipFile("./files/test.zip") as zip_file:
#     zip_file.printdir()

# with ZipFile("./files/test.zip") as zip_file:
#     info = zip_file.infolist()
#     print(info[6].filename)
#     print(info[6].compress_type)
#     print(info[6].file_size)
#     print(info[6].compress_size)
#     print(info[6].date_time)
#     print(info[6].is_dir())

# with ZipFile("./files/test.zip") as zip_file:
#     # return name list files
#     info = zip_file.namelist()
#     print(info)


# with ZipFile("./files/test.zip") as zip_file:
#     # return name list files
#     info = zip_file.namelist()
#     last_file = zip_file.getinfo(info[-4])
#     print(last_file)

# Работа с конкретными файлами из архива.
with ZipFile("./files/test.zip") as zip_file:
    # zip_file.printdir()
    with zip_file.open("test/Разные файлы/astros.json") as file_json:
        print(file_json.read())
