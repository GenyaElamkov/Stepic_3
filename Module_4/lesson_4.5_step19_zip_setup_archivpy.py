"""
Создал архив files.zip и добавил в него все файлы из данного списка.
"""

from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf',
              'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py',
              'test.py']

with ZipFile("files.zip", mode="w") as zip_file:
    # for file_name in file_names:
    #     file_path = f"dir/{file_name}"
    #     with open(file_path, "w") as file:
    #         zip_file.write(file_path)
    for file_name in file_names:
        zip_file.write(file_name)
