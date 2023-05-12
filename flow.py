#####################################################
# Модуль 4.1 потоковый ввод stdin и вывод stdout    #
#####################################################
import csv
import sys
from datetime import datetime


def reverse_order():
    """
    Выводит все введенные строки, предварительно расположив в каждой
    строке все символы в обратном порядке.
    """

    # for line in sys.stdin:
    #     print(line.strip('\n')[::-1])

    txt = [line[::-1].strip() for line in sys.stdin.readlines()]
    print(*txt, sep='\n')


# reverse_order()

def data_scope():
    """
    Выводит единственное число — количество дней между максимальной
    и минимальной датами введенной последовательности.
    """
    pattern = '%Y-%m-%d'
    dts = list(map(str.strip, sys.stdin))
    dt_max = datetime.strptime(max(dts), pattern)
    dt_min = datetime.strptime(min(dts), pattern)

    print((dt_max - dt_min).days)

    # date = [datetime.fromisoformat(i.strip()) for i in sys.stdin]


# data_scope()


def three_socks_lemma(socs):
    """
    Определяет победителя в игре, правила которой представлены
    в условии задачи, и вывести его имя.
    """

    dima_even = len(socs) % 2 == 0 and socs[-1] % 2 == 0
    dima_odd = len(socs) % 2 > 0 and socs[-1] % 2 > 0

    name = 'Анри'
    if dima_even or dima_odd:
        name = 'Дима'

    return name


# socs = list(map(int, sys.stdin))
# socs = [1, 3, 5, 10, 3, 2, 12]
# print(three_socks_lemma(socs))


def statistics_lesson(socs):
    """
    Определяет рост самого низкого и самого высокого учеников,
    а также средний рост среди всех учеников.
    """
    socs = list(map(int, socs))
    if not socs:
        return "нет учеников"
    low_man = f"Рост самого низкого ученика: {min(socs)}"
    tall_man = f"Рост самого высокого ученика: {max(socs)}"
    average_man = f"Средний рост: {sum(socs) / len(socs)}"
    # return f"{low_man}\n{tall_man}\n{average_man}"
    # print(f"{low_man}\n{tall_man}\n{average_man}")

    return f"{low_man} {tall_man} {average_man}"


# socs = list(map(int, sys.stdin))
# socs = []

# print(statistics_lesson(socs))


def commentator():
    """
    Выводит единственное число — количество строк в введенном коде,
    которые содержат в себе только комментарии.
    """
    counter = 0
    for line in sys.stdin:
        if line.strip().startswith('#'):
            counter += 1
    print(counter)

    # print(sum(1 for row in stdin if row.lstrip().startswith('#')))


# commentator()

def no_commentator():
    """
    Выводит введенный блок кода, предварительно удалив из него все строки
    которые содержат в себе только комментарии.
    """
    for line in sys.stdin:
        if line.lstrip(' ')[0] != '#':
            print(line.rstrip('\n'))

    # print(*[line.rstrip('\n') for line in sys.stdin if line.lstrip(' ')[0] != '#'], sep='\n')


# no_commentator()

def panoramic_agency():
    """
    Выводит все новости, которые относятся к введенной категории.
    Новости должны быть расположены в порядке возрастания степени
    достоверности, а при совпадении степеней достоверности —
    в лексикографическом порядке самих новостей.
    """
    dic = {}
    key = ''
    for line in sys.stdin:
        try:
            keys = line.split('/')[-2].strip()
            print(keys)
            dic[keys] = dic.setdefault(keys, []) + [line]
        except IndexError:
            key = line

    for line in sorted(sorted(dic[key]), key=lambda x: x.split('/')[-1]):
        print(line.split('/')[0].strip())


# panoramic_agency()


def python(socs):
    """
    Определяет, в каком порядке расположены даты в данной последовательности.
    """
    pattern = '%d.%m.%Y'

    dts = [datetime.strptime(dt.strip(), pattern) for dt in sys.stdin]

    if sorted(set(dts)) == dts:
        res = 'ASC'
    elif sorted(set(dts), reverse=True) == dts:
        res = 'DESC'
    else:
        res = 'MIX'

    print(res)
    # return res


# socs = list(map(str, sys.stdin))
# socs = ["14.06.2022",
#         "20.06.2022",
#         "21.06.2022"]
# python(socs)

def guru_progressions(socs):
    """
    Определяет, является ли данная последовательность прогрессией,
    и если да, то определяет её вид.
    """

    nums = list(map(int, socs))
    # nums = list(map(int, sys.stdin))

    ratio = nums[1] / nums[0]
    arr = []
    for i in range(1, len(nums)):
        res = False
        if nums[i] / nums[i - 1] == ratio:
            res = True
        arr.append(res)

    if all(arr):
        print('Геометрическая прогрессия')
    elif list(range(nums[0], nums[-1] + 1)) == nums:
        print('Арифметическая прогрессия')
    else:
        print('Не прогрессия')


# socs = [2, 4, 8, 16]
# guru_progressions(socs)
#####################################################
# Модуль 4.2 работа с csv файлами.                  #
#####################################################

def seales():
    """
    Выводит названия тех товаров, цена на которые уменьшилась/
    """
    with open('files/sales.csv', 'r', encoding='utf-8') as csv_file:
        rows = csv.DictReader(csv_file, delimiter=';')
        for row in rows:
            if int(row['new_price']) < int(row['old_price']):
                print(row['name'])


# seales()

def average_salary():
    """
    Упорядочивает компании по возрастанию средней зарплаты ее сотрудников
    и выводит их названия, каждое на отдельной строке. Если две компании
     имеют одинаковые средние зарплаты, они должны быть расположены
     в лексикографическом порядке их названий.
    """
    with open('files/salary_data.csv', 'r', encoding='utf-8') as csv_file:
        rows = csv.DictReader(csv_file, delimiter=';')
        dic = {}
        # Добавляем в словарь, список значений по ключу.
        for row in rows:
            dic.setdefault(row['company_name'], []).append(int(row['salary']))
    # Среднее значение.
    avrg_dic = {k: int(sum(v) / len(v)) for k, v in dic.items()}
    print(*sorted(avrg_dic, key=avrg_dic.get), sep='\n')


# average_salary()

def sorting_column():
    with open('files/deniro.csv', 'r', encoding='utf-8') as csv_file:
        """
        Если определить list, то можно обрщаться с context как к списку
        context = list(csv.reader(csv_file))
        context.sort(key=lambda x: int(x[i]) if x[i].isdigit() else x[i])
        for lst in context:
            print(*lst, sep=',')
        """
        context = csv.reader(csv_file)

        col = int(input()) - 1
        content = sorted(context,
                         key=lambda x: int(x[col])
                         if x[col].isdigit() else x[col])

    [print(','.join(line)) for line in content]


# sorting_column()

def csv_columns(filename: str) -> dict:
    """
    Возвращать словарь, в котором ключом является название столбца файла
    filename, а значением — список элементов этого столбца.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        context = csv.DictReader(csv_file, delimiter=',')
        header = context.fieldnames
        dic = {}
        for line in context:
            for h in header:
                dic[h] = dic.setdefault(h, []) + [line[h]]
    return dic

    # with open(filename, 'r', encoding='utf-8') as file:
    #     reader = csv.DictReader(file, delimiter=',')
    #     d = {}
    #     for row in reader:
    #         for key, value in row.items():
    #             d[key] = d.get(key, []) + [value]
    #     return d


# filename = 'files/exam.csv'
# print(csv_columns(filename))

def popular_domains():
    """
    domain,count
    rambler.ru,24
    iCloud.com,29
    """
    with open('files/data.csv', 'r', encoding='utf-8') as csv_file:
        content = csv.reader(csv_file)
        dic = {}
        for index, text in enumerate(content):
            if index == 0:
                continue
            domen = text[2].split('@')[1]
            dic[domen] = dic.get(domen, 0) + 1

    colums = ['domain', 'count']

    with open('domain_usage.csv', 'w', encoding='utf-8',
              newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(colums)
        for row in sorted(sorted(dic.items()), key=lambda x: x[1]):
            writer.writerow(row)


# popular_domains()

def wifi():
    """
     Определяет количество точек доступа в каждом районе Москвы и
     выводит названия всех районов, для каждого указывая соответствующее
     количество точек доступа.
    """
    with open('files/wifi.csv', 'r', encoding='utf-8') as f:
        contex = csv.reader(f, delimiter=';')
        dic = {}
        for index, data in enumerate(contex):
            if index == 0:
                continue
            dic[data[1]] = dic.setdefault(data[1], 0) + int(data[3])

    # Сортировка по убыванию lambda x: -x[1], не используя reverse.
    [print(f'{k}: {v}') for k, v in
     sorted(sorted(dic.items()), key=lambda x: -x[1])]


# wifi()

def last_day_on_Titanic():
    """
    Выводит имена выживших пассажиров, которым было менее
    18 лет, каждое на отдельной строке. Причем сначала должны быть расположены
    имена всех пассажиров мужского пола, а затем — женского, имена же
    непосредственно в мужском и женском списках должны быть расположены в
    своем исходном порядке.
    """
    sex_man = []
    sex_woman = []
    survived = '1'
    with open('files/titanic.csv', 'r', encoding='utf-8') as f:
        for data in csv.DictReader(f, delimiter=';'):
            if float(data['age']) >= 18:
                continue
            if data['sex'] == 'male' and data['survived'] == survived:
                sex_man.append(data['name'])
            if data['sex'] == 'female' and data['survived'] == survived:
                sex_woman.append(data['name'])
    print(*sex_man, sep='\n')
    print(*sex_woman, sep='\n')


# last_day_on_Titanic()

def log_file():
    """
    Отбирает из файла name_log.csv только самые свежие записи для
    каждого пользователя и записывает их в файл new_name_log.csv.
    """
    dic = {}
    with open('files/name_log.csv', 'r', encoding='utf-8') as f:
        header, *context = list(csv.reader(f, delimiter=','))
        for data in sorted(context, key=lambda x: x[2], reverse=True):
            dic[data[1]] = dic.setdefault(data[1], data)

    with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in sorted(dic.values(), key=lambda x: x[1]):
            writer.writerow(row)
        # Заместо цикла.
        # w.writerows(sorted(d.values(), key=lambda x: x[1]))


# log_file()

# Мой вариант решения.
def condense_csv(filename, id_name):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = list(csv.reader(f, delimiter=','))

        tmp_dict = {}
        arr = []
        k = reader[0][0]
        header = [id_name]
        for i, text in enumerate(reader, 1):
            if text[0] != k:
                arr.append(tmp_dict)
                tmp_dict = {}
                k = text[0]

            tmp_dict[id_name] = tmp_dict.setdefault(id_name, text[0])
            tmp_dict[text[1]] = tmp_dict.setdefault(text[1], text[2])

            if len(reader) == i:
                arr.append(tmp_dict)
            if text[1] not in header:
                header.append(text[1])

        # header = []
        # for dic in arr:
        #     for key in dic.keys():
        #         if key not in header:
        #             header.append(key)

        with open('condensed.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, delimiter=',', fieldnames=header)
            writer.writeheader()
            for dic in arr:
                writer.writerow(dic)


# Вариант решения 1 со вложенными словарями.
# def condense_csv(filename, id_name):
#     with open(filename, encoding='utf-8') as file:
#         objects = {}
#         for obj, attr, value in csv.reader(file):
#             if obj not in objects:
#                 objects[obj] = {id_name: obj}
#             objects[obj][attr] = value
#         pprint(objects)
#     with open('condensed.csv', 'w', encoding='utf-8', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=objects[obj])
#         writer.writeheader()
#         writer.writerows(objects.values())

#  Вариант решения 2
# def condense_csv(filename, id_name):
#     objects = {}
#     with open(filename, encoding='utf-8') as infile:
#         reader = csv.reader(infile, delimiter=',')
#         for obj, prop, val in reader:
#             objects.setdefault(obj, {}).setdefault(prop, val)
#
#     with open("condensed.csv", encoding='utf-8', mode="w", newline='') as outfile:
#         writer = csv.writer(outfile, delimiter=',')
#         writer.writerow((id_name, *objects[obj].keys()))
#         for key in objects:
#             writer.writerow((key, *objects[key].values()))

filename, id_name = "files/data_1.csv", 'ID'
condense_csv(filename, id_name)
