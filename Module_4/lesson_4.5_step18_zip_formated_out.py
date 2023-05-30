"""
Выводит названия всех файлов из этого архива в лексикографическом порядке,
указывая для каждого его дату изменения, а также объем до и после сжатия,
в следующем формате:

<название файла>
  Дата модификации файла: <дата изменения>
  Объем исходного файла: <объем до сжатия> байт(а)
  Объем сжатого файла: <объем после сжатия> байт(а)

https://stepik.org/lesson/547172/step/18?unit=540798
"""

from datetime import datetime
from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    info = zip_file.infolist()
    for item in sorted(info, key=lambda x: x.filename.split('/')[-1]):
        if not item.is_dir():
            print(f"{item.filename.split('/')[-1]}")
            print(f"  Дата модификации файла: {datetime(*item.date_time)}")
            print(f"  Объем исходного файла: {item.file_size} байт(а)")
            print(f"  Объем сжатого файла: {item.compress_size} байт(а)")
            print()
