"""
Выводит названия файлов из этого архива, которые были созданы или изменены
позднее 2021-11-30 14:22:00. Названия файлов должны быть расположены в
лексикографическом порядке, каждое на отдельной строке.

https://stepik.org/lesson/547172/step/17?unit=540798
"""

from datetime import datetime
from zipfile import ZipFile

flag_date = datetime.strptime("2021-11-30 14:22:00", "%Y-%m-%d %H:%M:%S")
with ZipFile("workbook.zip") as zip_file:
    result = []
    for item in zip_file.infolist():
        if not item.is_dir() and datetime(*item.date_time) > flag_date:
            result.append(item.filename.split('/')[-1])

print(*sorted(result), sep='\n')
