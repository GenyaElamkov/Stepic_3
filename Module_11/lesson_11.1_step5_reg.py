"""
Я в аду?
Напишите программу, которая в заданном тексте находит все телефонные номера, соответствующие следующим форматам:

7-ddd-ddd-dd-dd
8-ddd-dddd-dddd
где d — цифра от 
0 до 9.

Формат входных данных
На вход программе подается строка произвольного содержания.

Формат выходных данных
Программа должна в введенном тексте найти все телефонные номера, соответствующие форматам, указанным в условии задачи, и вывести их в том порядке, в котором они были найдены, каждый на отдельной строке.

https://stepik.org/lesson/640164/step/6?unit=636683
"""


txt = "Тимур: 7-ddd-ddd-dd-dd, Сослан: 8-ddd-dddd-dddd, Артур: 7-123-123-11-22,,,, Дима: 8-123-123-11-22, Анри: 8-123-1231-1221...... Гвидо: 7-123-1231-1221, 7-123-13-181-22, 8-1237-131-1221"
# txt = "Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911"

for chunk in txt.split():
    phone_status = False
    if chunk.startswith(("7-", "8-", "+7-", "+8-")):
        chunk = "".join(filter(lambda x: x not in (",", ".", "+"), chunk))

        nums_true = sum(char.isdigit() for char in chunk) >= 10
        if not nums_true:
            continue

        chunk_arr = chunk.split("-")
        if chunk_arr[0] == "7":
            phone_status = (
                len(chunk_arr[1]) == 3
                and len(chunk_arr[2]) == 3
                and len(chunk_arr[3]) == 2
                and len(chunk_arr[4]) == 2
            )

        if chunk_arr[0] == "8":
            phone_status = (
                len(chunk_arr[1]) == 3
                and len(chunk_arr[2]) == 4
                and len(chunk_arr[3]) == 4
            )
    if phone_status:
        print(chunk)
