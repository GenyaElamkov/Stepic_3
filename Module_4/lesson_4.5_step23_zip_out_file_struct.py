"""
Выводит его файловую структуру и объем каждого файла.

https://stepik.org/lesson/547172/step/23?unit=540798
"""

from zipfile import ZipFile


def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'


def main():
    with ZipFile("desktop.zip") as zip_file:
        info = zip_file.infolist()

        for items in info:
            res = list(filter(None, items.filename.split('/')))
            size = convert_bytes(items.file_size)

            if len(res) == 1:
                result = res[0]
            if len(res) >= 2:
                result = f"{' ' * ((len(res) - 1) * 2)}{res[-1]}"
            if not items.is_dir():
                result += f" {size}"

            print(result)


if __name__ == "__main__":
    main()
