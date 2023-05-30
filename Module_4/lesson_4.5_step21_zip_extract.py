"""
Извлекать файлы *args из архива zip_name в папку с программой.
Если в функцию не передано ни одного названия файла для извлечения,
то функция должна извлечь все файлы из архива.

https://stepik.org/lesson/547172/step/21?unit=540798
"""

from zipfile import ZipFile

def extract_this(zip_name, *args):
    with ZipFile(zip_name, mode="a") as zip_file:
        if not args:
            zip_file.extractall()
        else:
            for file in args:
                zip_file.extract(file)

#
# def extract_this(zip_name: str, *args):
#     if not args:
#         args = None
#     with ZipFile(zip_name) as zf:
#         zf.extractall(members=args)



if __name__ == "__main__":
    extract_this('workbook.zip', 'earth.jpg', 'exam.txt')
    # extract_this('workbook.zip')
