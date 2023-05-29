"""
Выводит название файла из этого архива, который имеет наилучший
показатель степени сжатия.
"""


from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    info = zip_file.infolist()

    largest = 0
    filename = ''
    for item in info:
        if not item.is_dir():
            resoult = 100 - ((item.compress_size / item.file_size) * 100)
            if largest <= resoult:
                largest = resoult
                filename = item.filename
    print(filename.split('/')[-1])
