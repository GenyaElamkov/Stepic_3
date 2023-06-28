"""
Самостоятельное изучение.

https://stepik.org/lesson/737724/step/1?unit=739371
"""
import os

""""
Модуль os.

https://all-python.ru/osnovy/os.html
"""
# Имя OC
# print(os.name) # nt -> Windows

# Переменное окружение
# print(os.environ)

# Доступ к переменной окружения по ключу.
# print(os.getenv("TMP"))

# Изменение рабочей директории.
print(os.getcwd())  # -> полный путь

os.chdir("../Module_4/files")  # Изменяем рабочую диреуторию.
print(os.getcwd())

# Проверка существования пути.
print(os.path.exists("D:\python_2022\Stepic_3\Module_4"))

# Существует файл.
print(os.path.isfile("D:\python_2022\Stepic_3\Module_4\dogs.pkl"))
# Существует директория.
print(os.path.isdir("D:\python_2022\Stepic_3\Module_4"))

# Создание директорий
# os.mkdir(r"D:\python_2022\Stepic_3\Module_4\folder")

# Создание цепочки директорий
# os.makedirs(r"D:\python_2022\Stepic_3\Module_4\folder\test_1\test2")

# Удаление файлов.
# os.remove(r"D:\python_2022\Stepic_3\Module_4\folder\test_1\test2\test.txt")
# Удвление пустой директории.
# os.rmdir(r"D:\python_2022\Stepic_3\Module_4\folder\test_1\test2")
# os.removedirs(r"D:\python_2022\Stepic_3\Module_4\folder\test_1")

# Запуск на исполнение
# os.startfile("D:\python_2022\Stepic_3\Module_4\data.zip")

# Получение имени файла и директории.
print(os.path.basename("D:\python_2022\Stepic_3\Module_4"))
print(os.path.dirname("D:\python_2022\Stepic_3\Module_4"))

# Вычисление размера.
print(os.path.getsize("D:\python_2022\Stepic_3\Module_4\data.zip"))

# Переименование директории
# os.rename(r"D:\python_2022\Stepic_3\Module_4\folder", r"D:\python_2022\Stepic_3\Module_4\test_1")
# Переименование диреукторий
# os.renames(r"D:\python_2022\Stepic_3\Module_4\folder", r"D:\python_2022\Stepic_3\Module_4\test_1")

# Содержимое директорий
# print(os.listdir("D:\python_2022\Stepic_3\Module_4"))

# Получаем содержимое всех директорий
# print(list(os.walk("D:\python_2022\Stepic_3\Module_4")))

# Информация о файлах и директориях.
print(os.stat("D:\python_2022\Stepic_3\Module_4"))

# Обработка путей.
print(os.path.split("D:\python_2022\Stepic_3\Module_4"))    # Разединяем путь.
print(os.path.join("D:\python_2022\Stepic_3", "Module_4"))  # Соединяем путь.

