"""
выводит суммарный объем файлов этого архива в сжатом и не сжатом видах в байтах, в следующем формате:

Объем исходных файлов: <объем до сжатия> байт(а)
Объем сжатых файлов: <объем после сжатия> байт(а)
"""

from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    info = zip_file.infolist()
    files_sizes = sum([item.file_size for item in info])
    compress_sizes = sum([item.compress_size for item in info])

print(f"Объем исходных файлов: {files_sizes} байт(а)")
print(f"Объем сжатых файлов: {compress_sizes} байт(а)")
