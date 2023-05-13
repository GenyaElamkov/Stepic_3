#####################################################
# Модуль 4.2 работа с csv файлами.                  #
#####################################################

def seales():
    """
    Выводит названия тех товаров, цена на которые уменьшилась/
    """
    with open('../files/sales.csv', 'r', encoding='utf-8') as csv_file:
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
    with open('../files/salary_data.csv', 'r', encoding='utf-8') as csv_file:
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
    with open('../files/deniro.csv', 'r', encoding='utf-8') as csv_file:
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
    with open('../files/data.csv', 'r', encoding='utf-8') as csv_file:
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
    with open('../files/wifi.csv', 'r', encoding='utf-8') as f:
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
    with open('../files/titanic.csv', 'r', encoding='utf-8') as f:
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
    with open('../files/name_log.csv', 'r', encoding='utf-8') as f:
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


# condense_csv(filename, id_name)

def student_counts():
    """
    Зписывает данную таблицу в файл sorted_student_counts.csv,
    располагая все столбцы в порядке возрастания классов,
     при совпадении классов — в порядке возрастания букв.
    """
    with open('../files/student_counts.csv', 'r', encoding='utf-8') as f, \
            open('sorted_student_counts.csv', 'w', encoding='utf-8',
                 newline='') as out_f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        header = header[:1] + sorted(sorted(header[1:]),
                                     key=lambda x: int(x.split('-')[0]))

        writer = csv.DictWriter(out_f, delimiter=',', fieldnames=header)
        writer.writeheader()
        writer.writerows(reader)
        # for rows in reader:
        #     writer.writerow(rows)


# student_counts()

def student_hungry():
    with open('../files/prices.csv', 'r', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        header = ''.join(reader[0]).split(';')
        cheap_products = []
        for line in reader[1:]:
            arr_prices = ''.join(line).split(';')
            min_price = min(map(int, arr_prices[1:]))
            product = header[arr_prices.index(str(min_price))]
            cheap_products.append((min_price, product, arr_prices[0]))

    print(*min(cheap_products, key=lambda x: x[0])[1:], sep=': ')

# Вариант решения задачи.
# with open('prices.csv', encoding='UTF-8') as f:
#     h, *rows = csv.reader(f, delimiter=';')
#
# goods = [(r[0], h[x], r[x]) for r in rows for x in range(1, len(h))]
# cheapest = min(goods, key=lambda x: (int(x[2]), x[1], x[0]))
#
# print(f'{cheapest[1]}: {cheapest[0]}')

# student_hungry()
