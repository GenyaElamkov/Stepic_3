"""
Модуль shutil

https://stepik.org/lesson/737724/step/1?unit=739371
"""

import shutil
import os

# os.mkdir("Folder")

file_name = "Folder/test.txt"
out_file = "Folder/test_2.txt"
dir_tree = "Folder"
out_dir = "Folder/Test"
# Копировать файлы, не все копируются методанные.
# shutil.copy(file_name, out_file)

# Копировать файлы с методанными
# shutil.copy2(file_name, out_file)

# Копируем имена файлов.
# res = shutil.copyfile(file_name, out_file)

# Копируем дерево.
# shutil.copytree(dir_tree, out_dir)

# Удаления файла или подкатолога. Если нет FileNotFoundError
# shutil.rmtree(out_dir)

# Поиск пути.
# print(shutil.which(file_name))

# Размер диска.
# print(shutil.disk_usage(dir_tree))

# Перемещение файлов.
# shutil.move(out_file, out_dir)

# Создаем архив. Возвращает имя.
print(shutil.make_archive("hello", "zip", dir_tree))

# Показывает все поддерживаемые форматы архивов в файле или каталоге.
print(shutil.get_archive_formats())