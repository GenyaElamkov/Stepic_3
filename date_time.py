import calendar
import time
from datetime import date
from datetime import datetime
# from datetime import time
from datetime import timedelta
from math import ceil


# import time


#####################################################
# Модуль 3.1 Тема урока: типы данных date и time.   #
#####################################################

def quarter():
    """
    Вам доступен список dates, содержащий даты. Дополните приведенный ниже
    код, чтобы он вывел год и номер квартала каждой даты из данного списка.
    Компоненты дат должны быть расположены в исходном порядке, каждые на
    отдельной строке, в следующем формате:

    <год>-Q<номер квартала>
    """

    dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25),
             date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13),
             date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19),
             date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

    print(*[f"{d.year}-Q{ceil(d.month / 3)}" for d in dates], sep='\n')


def get_min_max(dates):
    """
    Реализуйте функцию get_min_max(), которая принимает один аргумент:

    dates — список дат (тип date) Функция должна возвращать кортеж, первым
    элементом которого является минимальная дата из списка dates, вторым —
    максимальная дата из списка dates. Если список dates пуст, функция должна
    вернуть пустой кортеж.
    """
    return (min(dates), max(dates)) if dates else ()


def get_date_range(start_date, end_date):
    """
    Реализуйте функцию get_date_range(), которая принимает два аргумента в
    следующем порядке:

    start — начальная дата, тип date end — конечная дата, тип date Функция
    get_date_range() должна возвращать список, состоящий из дат (тип date) от
    start до end включительно. Если start > end, функция должна вернуть пустой
    список.
    """

    # при использовании генератора при не возможности перебрать получается
    # пустой список.
    return [date.fromordinal(_) for _ in range(start_date.toordinal(),
                                               end_date.toordinal() + 1)]


def saturdays_between_two_dates(start_date: date, end_date: date) -> int:
    """
    Реализуйте функцию saturdays_between_two_dates(), которая принимает два
    аргумента в следующем порядке:

    start — начальная дата, тип date end — конечная дата, тип date Функция
    должна возвращать количество суббот между датами start и end включительно.

    Примечание 1. Даты могут передаваться в любом порядке, то есть не
    гарантируется, что первая дата меньше второй.
    """

    if start_date > end_date:
        start_date, end_date = end_date, start_date

    saturday = 6
    counter_saturday = 0
    for d in range(start_date.toordinal(), end_date.toordinal() + 1):
        if date.fromordinal(d).isoweekday() == saturday:
            counter_saturday += 1

    return counter_saturday
    # Еще один вариант. return sum(date.fromordinal(d).isoweekday() ==
    # saturday for d in range(start_date.toordinal(), end_date.toordinal() +
    # 1))


#####################################################
# Модуль 3.2 Тема урока: типы данных date и time.   #
#####################################################

def set_two_date():
    """
    Напишите программу, которая принимает на вход две даты и выводит ту,
    что меньше.
    """
    date_iso = [date.fromisoformat(input()) for _ in range(2)]
    print(min(date_iso).strftime("%d-%m (%Y)"))


def sorting_date():
    """
    Напишите программу, которая принимает на вход последовательность дат и
    выводит их в порядке неубывания.
    """
    date_array = [date.fromisoformat(input()) for _ in range(int(input()))]
    print(*[fd.strftime('%d/%m/%Y') for fd in sorted(date_array)], sep='\n')


def print_good_dates(dates: list) -> None:
    """
    Тимур считает дату «интересной», если её год совпадает с годом его
    рождения, а сумма номера месяца и номера дня равна его возрасту. Год
    рождения Тимура — 19921992, возраст — 2929 лет.

    Реализуйте функцию print_good_dates(), которая принимает один аргумент:

    dates — список дат (тип date) Функция должна выводить «интересные» даты
    в порядке возрастания, каждую на отдельной строке, в формате  month_name
    DD, YYYY, где month_name — полное название месяца на английском.
    """
    YEAR = 1992
    AGE = 29
    intrstng_dt = [d for d in dates if
                   d.year == YEAR and sum([d.month, d.day]) == AGE]

    print(*[fd.strftime('%B %d, %Y') for fd in sorted(intrstng_dt)], sep='\n')


def is_correct(day: int, month: int, year: int) -> bool:
    """
    Реализуйте функцию is_correct(), которая принимает три аргумента в
    следующем порядке:

    day — натуральное число, день month — натуральное число, месяц year —
    натуральное число, год Функция должна возвращать True, если дата с
    компонентами day, month и year является корректной, или False в противном
    случае.
    """
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False


def corrections_data():
    """
    Напишите программу, которая принимает на вход последовательность дат и
    проверяет каждую из них на корректность.
    """
    count_correct_data = 0
    while True:
        try:
            day, moth, year = list(map(int, input().split('.')))
        except ValueError:
            print(count_correct_data)
            break

        if is_correct(day, moth, year):
            count_correct_data += 1
            print("Корректная")
        else:
            print("Некорректная")


#####################################################
# Модуль 3.3 Тема урока: тип данных datetime.       #
#####################################################

def shop():
    """
    Вам доступен список times_of_purchases, содержащий даты (тип datetime),
    в которые были совершены покупки в некотором интернет-магазине.
    Дополните приведенный ниже код, чтобы он вывел текст До полудня,
    если большее число покупок было совершено до полудня, или текст После
    полудня в противном случае.
    """
    times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25),
                          datetime(2017, 10, 1, 15, 26, 26),
                          datetime(2017, 10, 1, 15, 42, 57),
                          datetime(2017, 10, 1, 17, 49, 59),
                          datetime(2017, 10, 2, 6, 37, 10),
                          datetime(2017, 10, 2, 6, 42, 53),
                          datetime(2017, 10, 2, 8, 56, 45),
                          datetime(2017, 10, 2, 9, 18, 3),
                          datetime(2017, 10, 2, 12, 23, 48),
                          datetime(2017, 10, 2, 12, 45, 5),
                          datetime(2017, 10, 2, 12, 48, 8),
                          datetime(2017, 10, 2, 12, 10, 54),
                          datetime(2017, 10, 2, 19, 18, 10),
                          datetime(2017, 10, 2, 12, 31, 45),
                          datetime(2017, 10, 3, 20, 57, 10),
                          datetime(2017, 10, 4, 7, 4, 57),
                          datetime(2017, 10, 4, 7, 13, 31),
                          datetime(2017, 10, 4, 7, 13, 42),
                          datetime(2017, 10, 4, 7, 21, 54),
                          datetime(2017, 10, 4, 14, 22, 12),
                          datetime(2017, 10, 4, 14, 50),
                          datetime(2017, 10, 4, 15, 7, 27),
                          datetime(2017, 10, 4, 12, 44, 49),
                          datetime(2017, 10, 4, 12, 46, 41),
                          datetime(2017, 10, 4, 16, 32, 33),
                          datetime(2017, 10, 4, 16, 34, 44),
                          datetime(2017, 10, 4, 16, 46, 59),
                          datetime(2017, 10, 4, 12, 26, 6)]
    HOUR = 12
    MINUTE = 0
    afternoon = list(filter(lambda dt: dt.hour >= HOUR and dt.minute > MINUTE,
                            times_of_purchases))
    tmp = [dt.strftime('%p') for dt in times_of_purchases]
    print(tmp)
    afternoon_true = len(times_of_purchases) - len(afternoon) > len(afternoon)
    print("До полудня" if afternoon_true else "После полудня")


def all_datetime():
    """
    Вам доступны список dates, содержащий даты, и список times, содержащий
    времена. Количество элементов в этих списках одинаковое. Дополните
    приведенный ниже код, чтобы он вывел datetime объекты, полученные путем
    объединения элементов списков dates и times, находящихся на одинаковых
    позициях. Полученные объекты должны быть расположены в порядке
    возрастания секунд, каждый на отдельной строке.
    """
    dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12),
             date(632, 6, 4),
             date(295, 1, 23), date(327, 8, 24), date(167, 4, 16),
             date(229, 1, 24),
             date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24),
             date(479, 9, 6)]

    times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47),
             time(20, 8, 59),
             time(12, 42, 56), time(15, 9, 57), time(17, 47, 9),
             time(9, 40, 2),
             time(11, 47, 1), time(17, 27, 10), time(17, 55, 40),
             time(9, 14, 9)]

    dt_combns = [datetime.combine(dt[0], dt[1]) for dt in zip(dates, times)]
    print(*sorted(dt_combns, key=lambda x: x.second), sep="\n")


def fast_code():
    """
    Ученики онлайн-школы BEEGEEK решили выяснить, кто из них быстрее всех
    решит домашнее задание по математике. Для этого каждый ученик
    зафиксировал время начала и окончания решения своей домашней работы.

    Вам доступен словарь data, содержащий результаты учеников. Ключом в словаре
    является имя ученика, а значением — кортеж, первый элемент которого — время
    начала решения, второй элемент — время окончания решения. Дополните
    приведенный ниже код, чтобы он вывел имя ученика, который затратил на
    решение домашнего задания меньше всего времени.
    """
    data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
            'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
            'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
            'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
            'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
            'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
            'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
            'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
            'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
            'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
            'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
    for k, val in data.items():
        start_time = datetime.strptime(val[0], '%d.%m.%Y %H:%M:%S').timestamp()
        finish_time = datetime.strptime(val[1],
                                        '%d.%m.%Y %H:%M:%S').timestamp()
        data[k] = finish_time - start_time

    print(min(data, key=data.get))


def cosmonaut_diary():
    """
    Вам доступен текстовый файл diary.txt, в который космонавт записывал
    небольшие отчёты за день. Каждый новый отчёт он мог записать либо в
    начало файла, либо в середину, либо в конец. Все отчеты разделены между
    собой пустой строкой. Каждый новый отчёт начинается со строки с датой и
    временем в формате DD.MM.YYYY; HH:MM, после которой следуют события,
    произошедшие за указанный день:
    """
    dic = dict()
    pattern = "%d.%m.%Y; %H:%M"

    with open("files/diary.txt", "r", encoding="utf-8") as f:
        content = f.read().split('\n\n')
        for w in content:
            key = w.split("\n")[0]
            dt_key = datetime.strptime(key, pattern).timestamp()
            dic[dt_key] = w[len(key) + 1:]

    for k, v in sorted(dic.items()):
        print(datetime.fromtimestamp(k).strftime(pattern))
        print(v)
        print()


def is_available_date(dates, some_date):
    """
    Во время визита очередного гостя сотрудникам отеля приходится проверять,
    доступна ли та или иная дата для бронирования номера.

    Реализуйте функцию is_available_date(), которая принимает два аргумента в
    следующем порядке:

    booked_dates — список строковых дат, недоступных для бронирования.
    Элементом списка является либо одиночная дата, либо период (две даты
    через дефис). Например: ['04.11.2021', '05.11.2021-09.11.2021']
    date_for_booking — одиночная строковая дата или период (две даты через
    дефис), на которую гость желает забронировать номер. Например:
    '01.11.2021' или '01.11.2021-04.11.2021' Функция is_available_date()
    должна возвращать True, если дата или период date_for_booking полностью
    доступна для бронирования. В противном случае функция должна возвращать
    False.
    """

    pattern = '%d.%m.%Y'

    some_date = some_date.split('-')
    p_some_dates = [datetime.strptime(dt, pattern) for dt in some_date]

    size_p_som_dates = 2
    if len(p_some_dates) == size_p_som_dates:
        start, finish = [dt.toordinal() for dt in p_some_dates]
        p_some_dates = [datetime.fromordinal(_) for _ in
                        range(start, finish + 1)]

    book_res = []
    size_date = 10
    for p_some_date in p_some_dates:
        for dts in dates:
            if len(dts) <= size_date:
                dt_true = datetime.strptime(dts, pattern) != p_some_date
            else:
                dts = dts.split('-')
                start_dt, finish_dt = [datetime.strptime(dt, pattern) for dt in
                                       dts]
                dt_true = (p_some_date < start_dt or p_some_date > finish_dt)
            book_res.append(dt_true)
    return all(book_res)


#####################################################
# Модуль 3.4 Тема урока: тип данных timedelta.      #
#####################################################
"""
Дополните приведенный ниже код, чтобы он прибавил к объекту 
datetime(2021, 11, 4, 13, 6) одну неделю и 1212 часов и вывел результат 
в формате DD.MM.YYYY HH:MM:SS.
"""
dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)
# print(dt.strftime('%d.%m.%Y %H:%M:%S'))

"""
Дополните приведенный ниже код, чтобы он вывел количество дней (целое число) 
между датами today и birthday.
"""
today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = birthday - today
# print(days.days)

"""
Напишите программу, которая принимает на вход дату и 
выводит предыдущую и следующую даты.
"""


# dt = datetime.strptime(input(), '%d.%m.%Y')
# dts = [dt - timedelta(days=1), dt + timedelta(days=1)]
# print(*[datetime.strftime(d, '%d.%m.%Y') for d in dts], sep='\n')


def number_of_seconds():
    """
    Напишите программу, которая принимает на вход время и выводит целое
    количество секунд, прошедшее с начала суток.
    """

    finish_time = input()

    pattern = '%H:%M:%S'
    start_time = '00:00:00'

    finish = datetime.strptime(finish_time, pattern)
    start = datetime.strptime(start_time, pattern)
    res_finish = timedelta(hours=finish.hour, minutes=finish.minute,
                           seconds=finish.second)
    res_start = timedelta(hours=start.hour, minutes=start.minute,
                          seconds=start.second)
    print((res_finish - res_start).seconds)

    # Вариант решения.
    # h, m, s = map(int, input().split(':'))
    #
    # td = timedelta(hours=h, minutes=m, seconds=s)
    #
    # print(int(td.total_seconds()))


def timer():
    """
    Часы показывают время в формате HH:MM:SS. На этих часах запустили таймер,
    который прозвенит через nn секунд. Напишите программу, которое определит,
    какое время будет на часах, когда прозвенит таймер.
    """
    h, m, s = map(int, input().split(':'))
    n = timedelta(seconds=int(input()))

    total_times = timedelta(hours=h, minutes=m, seconds=s) + n
    res_time = datetime.utcfromtimestamp((total_times.total_seconds()))

    print(res_time.time())

    # Вариант решения. dt = datetime.strptime(input(), pattern) + timedelta(
    # seconds=int(input())) print(dt.strftime(pattern))


def num_of_sundays(year: int) -> int:
    """
    Реализуйте функцию num_of_sundays(), которая принимает на вход один
    аргумент: year — натуральное число, год Функция должна возвращать
    количество воскресений в году year.
    """
    finish_month_year = 12
    finish_day_year = 31

    count_sunday = datetime(year=year, month=finish_month_year,
                            day=finish_day_year).strftime('%U')
    return int(count_sunday)


def productivity():
    """
    Артуру нужно подготовить 1010 задач для нового курса "ООП на Python".
    Чтобы занятие не оказалось утомительным, он придумал правило:

    если сегодня он подготовил первую задачу, то вторую он должен подготовить
    через один день если сегодня он подготовил вторую задачу, то третью он
    должен подготовить через два дня если сегодня он подготовил третью задачу,
    то четвертую он должен подготовить через три дня и так далее Напишите
    программу, которая определяет даты, в которые Артуру нужно подготовить задачи.
    """
    dates = input()

    pattern = '%d.%m.%Y'
    dt = datetime.strptime(dates, pattern)

    question = 10
    counter = 0
    while question != counter:
        dt_temp = dt + timedelta(days=counter)
        dt_finish = datetime(year=dt_temp.year, month=dt_temp.month,
                             day=dt_temp.day)
        dt = dt_finish + timedelta(days=1)
        counter += 1

        print(dt_finish.strftime(pattern))

    # Вариант решения.
    # pattern = '%d.%m.%Y'
    # dt = datetime.strptime(input(), pattern) - timedelta(days=1)
    #
    # for i in range(1, 11):
    #     dt += timedelta(days=i)
    #     print(dt.strftime(pattern))


def adjacent_dates():
    """
    Дана последовательность дат. Напишите программу, которая создает и
    выводит список, элементами которого являются неотрицательные целые
    числа — количество дней между двумя соседними датами последовательности.
    """
    "DD.MM.YYYY."

    res = list(
        map(lambda x: datetime.strptime(x, "%d.%m.%Y"), input().split()))
    print([abs(res[i - 1] - res[i]).days for i in range(1, len(res))])


def fill_up_missing_dates(dates: list) -> list:
    """
    Реализуйте функцию fill_up_missing_dates(), которая принимает на вход один
     аргумент:

    dates — список строковых дат в формате DD.MM.YYYY
    Функция должна возвращать список, в котором содержатся все даты из списка
    dates, расположенные в порядке возрастания, а также все недостающие
    промежуточные даты.
    """
    pattern = '%d.%m.%Y'

    dts = [datetime.strptime(d, pattern).toordinal() for d in dates]
    dt_max = max(dts)
    dt_min = min(dts)

    return [datetime.fromordinal(dt).strftime(pattern) for dt in
            range(dt_min, dt_max + 1)]


def matem():
    pattern_time = '%H:%M'
    start_time = datetime.strptime(input(), pattern_time)
    finish_time = datetime.strptime(input(), pattern_time)
    while start_time <= finish_time:
        lesson = start_time + timedelta(minutes=45)
        if lesson > finish_time:
            break
        print(
            f"{start_time.strftime(pattern_time)} - {lesson.strftime(pattern_time)}")

        start_time = lesson + timedelta(minutes=10)
    # Вариант решения.
    # f = '%H:%M'
    # start, stop = (datetime.strptime(input(), f) for i in '__')
    # while start <= (stop - timedelta(minutes=45)):
    #     print(start.strftime(f), '-',
    #           (start + timedelta(minutes=45)).strftime(f))
    #     start += timedelta(minutes=55)


def sum_data():
    data = [('07:14', '08:46'),
            ('09:01', '09:37'),
            ('10:00', '11:43'),
            ('12:13', '13:49'),
            ('15:00', '15:19'),
            ('15:58', '17:24'),
            ('17:57', '19:21'),
            ('19:30', '19:59')]
    pattern = '%H:%M'
    a = map(lambda x: datetime.strptime(x[1], pattern)
                      - datetime.strptime(x[0], pattern), data)
    print(int(sum(a, start=timedelta()).seconds / 60))


def get_days_week():
    """
    01.01.0001 по 31.12.9999
    13 день
    12 месяцев
    День недели числом 0-6, 0 — воскресенье
    """
    d = 13
    min_month = 1
    max_month = 12
    min_year = 1
    max_year = 9999
    count_days = {}
    for y in range(min_year, max_year + 1):
        for m in range(min_month, max_month + 1):
            friday = datetime(y, m, d).strftime('%u')
            count_days[friday] = count_days.get(friday, 0) + 1
    print(*[count_days[k] for k in sorted(count_days.keys())], sep='\n')


def again_time():
    """
    Выводит количество минут, которое осталось до закрытия
    магазина, или текст Магазин не работает, если он закрыт.
    """

    weekday = (timedelta(hours=9), timedelta(hours=21))
    weekend = (timedelta(hours=10), timedelta(hours=18))
    worktime = {"Mon": weekday, "Tue": weekday,
                "Wed": weekday, "Thu": weekday,
                "Fri": weekday, "Sat": weekend,
                "Sun": weekend}

    pattern = '%d.%m.%Y %H:%M'
    # data = input()
    data = '07.11.2021 10:00'
    dts = datetime.strptime(data, pattern)
    dt_name = dts.strftime('%a')

    dts_end = worktime[dt_name][1]
    dts_start = worktime[dt_name][0]
    dts_today = timedelta(hours=dts.hour, minutes=dts.minute)

    if dts_today >= dts_end or dts_today < dts_start:
        result = 'Магазин не работает'
    else:
        result = int((dts_end - dts_today).seconds / 60)

    print(result)


def most_understandable_condition():
    """
    Программа должна из указанного диапазона, включая концы, вывести,
    начиная с даты, у которой сумма дня и месяца нечетная, каждую третью дату,
    только если она не понедельник и не четверг. Даты должны быть расположены
    каждая на отдельной строке, в формате DD.MM.YYYY.
    """
    pattern = '%d.%m.%Y'

    left = datetime.strptime('30.04.2021', pattern)
    right = datetime.strptime('10.05.2021', pattern)

    while (left.day + left.month) % 2 == 0:
        left += timedelta(days=1)

    monday = 0
    thursday = 3
    for d in range(left.toordinal(), right.toordinal() + 1, 3):
        dt = datetime.fromordinal(d)
        if dt.weekday() == monday or dt.weekday() == thursday:
            continue

        print(dt.strftime(pattern))


def employees_organization_one():
    """
    Программа должна определить самого старшего сотрудника и вывести
    его дату рождения, имя и фамилию, разделив пробелом. Если таких
    сотрудников несколько, программа должна вывести их дату рождения,
    а также их количество, разделив пробелом.
    """
    pattern = '%d.%m.%Y'

    dic = {}
    for _ in range(int(input())):
        *name, birthday = input().split()
        dt = datetime.strptime(birthday, pattern)
        dic[dt] = dic.setdefault(dt, []) + [' '.join(name)]

    senior_employee = min(dic)
    birthday_senior = senior_employee.strftime(pattern)

    counter_senior = len(dic[senior_employee])
    if counter_senior > 1:
        result = f"{birthday_senior} {counter_senior}"
    else:
        result = f"{birthday_senior} {''.join(dic[senior_employee])}"

    print(result)


def employees_organization_two():
    """
    Программа должна вывести дату, в которую наибольшее количество сотрудников
    отмечает день рождения, в формате DD.MM.YYYY. Если таких дат несколько,
    программа должна вывести их все в порядке возрастания, каждую
    на отдельной строке, в том же формате.
    """
    pattern = '%d.%m.%Y'

    dic = {}
    for _ in range(int(input())):
        birthday = input().split()[-1]
        dt = datetime.strptime(birthday, pattern)
        dic[dt] = dic.get(dt, 0) + 1

    arr = []
    largest = dic[max(dic, key=dic.get)]
    for key in sorted(dic, key=dic.get, reverse=True):
        if largest > dic[key]:
            break
        arr.append(key)

    result = sorted(sorted(arr, key=lambda x: x.month), key=lambda x: x.year)
    print(*list(map(lambda x: x.strftime(pattern), result)), sep='\n')


def employees_organization_three():
    """
    Программа должна определить самого молодого сотрудника, празднующего
    свой день рождения в течение ближайших семи дней, и вывести его имя
    и фамилию, разделив пробелом. Если таких сотрудников нет, программа
    должна вывести текст:
    """

    # Определяем формат даты рождения '%d.%m.%Y'
    pattern = '%d.%m.%Y'

    # Вводим текущею дату.
    dt_start = datetime.strptime(input(), pattern)

    # Вводим кол-во сотрудников.
    # В цикле вводятся данные сотрудников. Имя Фамилия и дата рождения.
    dic = {}
    for _ in range(int(input())):
        *name, birthday = input().split()
        dt = datetime.strptime(birthday, pattern)
        dic[dt] = dic.setdefault(dt, ' '.join(name))

    # Устанавливаем конечную дату.
    end_dt = dt_start + timedelta(days=7)

    arr = []
    for d in dic.keys():
        # Сравниваем даты, заменяя год в дате рождения сотрудников.
        true_now_year = dt_start < d.replace(year=dt_start.year) <= end_dt
        true_next_year = dt_start < d.replace(year=dt_start.year + 1) <= end_dt
        if true_now_year or true_next_year:
            arr.append(d)

    result = 'Дни рождения не планируются'
    if arr:
        result = dic[max(arr)]

    print(result)


def choose_plural(amount, declensions):
    dic = {0: 2, 1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2,
           11: 2, 12: 2, 13: 2, 14: 2}

    num = int(str(amount)[-2:])
    if num in dic.keys():
        n = num
    else:
        n = amount % 10

    return f"{amount} {declensions[dic[n]]}"


def fake_news():
    """
    Программа должна вывести текст с указанием количества дней и часов,
    оставшихся до выхода курса.
    """
    pattern = "%d.%m.%Y %H:%M"
    dt_now = datetime.strptime(input(), pattern)

    dt_start = datetime.strptime("08.11.2022 12:00", pattern)

    res = dt_start - dt_now
    dt_hour = res.seconds // 3600
    dt_minute = res.seconds // 60 - (dt_hour * 60)
    dt_days = res.days

    plural_dict = {0: ("день", "дня", "дней"), 1: ("час", "часа", "часов"),
                   2: ("минута", "минуты", "минут")}
    text_day = choose_plural(dt_days, plural_dict[0])
    text_hour = choose_plural(dt_hour, plural_dict[1])
    text_minute = choose_plural(dt_minute, plural_dict[2])

    if dt_start > dt_now:
        if dt_days == 0 and dt_hour == 0:
            print(f"До выхода курса осталось: {text_minute}")
        elif dt_days == 0 and dt_minute == 0:
            print(f"До выхода курса осталось: {text_hour}")
        elif dt_hour == 0:
            print(f"До выхода курса осталось: {text_day}")
        elif dt_days == 0:
            print(
                f"До выхода курса осталось: {text_hour} и {text_minute}")
        else:
            print(
                f"До выхода курса осталось: {text_day} и {text_hour}")
    else:
        print("Курс уже вышел!")


#####################################################
# Модуль 3.6 Тема урока: модуль time                #
#####################################################
def add(a, b, c):
    time.sleep(7)
    return a + b + c


def add_one(a, b, c):
    time.sleep(5)
    return a + b + c


def calculate_it(func, *args) -> tuple:
    start = time.monotonic()
    result = func(*args)
    end = time.monotonic()
    res_sec = end - start
    return result, res_sec


# def calculate_it(func, *args) -> tuple:
#     start_time = time.perf_counter()
#     return (func(*args), time.perf_counter() - start_time)

def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


def get_the_fastest_func(funcs, *arg):
    times = []
    for func in funcs:
        start_time = time.perf_counter()
        func(*arg)
        end_time = time.perf_counter()

        res_time = end_time - start_time
        times.append(res_time)

    return funcs[times.index(min(times))]


#####################################################
# Модуль 3.7 Тема урока: модуль calendar            #
#####################################################

# import locale
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# print(calendar.calendar(2023, m=4))
day = calendar.day_name[1]


def leap_year():
    # for _ in range(int(input())):
    #     print(calendar.isleap(int(input())))

    print(*[calendar.isleap(int(input())) for _ in range(int(input()))],
          sep='\n')


def calendar_for_month():
    """
    Ввести календарь на введенные год и месяц.
    """

    year, month = input().split()
    month_index = list(calendar.month_abbr).index(month)
    # print(calendar.month(int(year), month_index))

    calendar.prmonth(int(year), month_index)


def day_week():
    # dt = datetime.strptime(input(), '%Y-%m-%d')
    # print(calendar.day_name[calendar.weekday(dt.year, dt.month, dt.day)])

    dt = datetime.fromisoformat(input())
    print(list(calendar.day_name)[dt.weekday()])


def number_days():
    """
    единственное число — количество дней в введенном месяце.
    """
    year, month = map(int, input().split())
    print(calendar.monthrange(year, month)[1])


def number_days_one():
    """
    вход полное название месяца
    единственное число — количество дней в введенном месяце.
    """
    year, month = input().split()
    month = list(calendar.month_name).index(month)
    print(calendar.monthrange(int(year), month)[1])


def get_days_in_month(year, month):
    """
    Возвращает отсортированный по возрастанию список всех дат (тип date)
    месяца month и года year.
    """
    month = list(calendar.month_name).index(month)

    return [date(year, month, dt) for dt in
            range(1, calendar.monthrange(year, month)[1] + 1)]


def get_all_mondays(year):
    """
    Возвращает отсортированный по возрастанию список всех дат (тип date)
    года year, выпадающих на понедельник.
    """
    mondays = []
    for m in range(1, 13):
        for d in calendar.monthcalendar(year, month=m):
            monday = d[0]
            if monday:
                mondays.append(date(year, m, monday))

    return mondays


def pm():
    """
    Третий четверг месяца.
    """
    year = int(input())
    pattern = '%d.%m.%Y'
    for m in range(1, 13):
        thursday = calendar.monthcalendar(year, m)[2][3]

        if calendar.monthcalendar(year, m)[0][3] == 0:
            thursday = calendar.monthcalendar(year, m)[3][3]

        print(datetime(year, m, thursday).strftime(pattern))

from datetime import datetime, date

#####################################################
# Модуль 3.8 Тема урока: модуль dateutil            #
#####################################################

from dateutil.relativedelta import relativedelta, FR, TU
from dateutil.easter import easter
from dateutil.parser import parse
from dateutil import rrule

# Создание нескольких объектов datetime для работы
dt_now = datetime.now()
print("Дата и время прямо сейчас:", dt_now)
dt_today = date.today()
print("Дата сегодня:", dt_today)

# Следующий месяц
print(dt_now + relativedelta(months=+1))

# Следующий месяц, плюс одна неделя
print(dt_now + relativedelta(months=+1, weeks=+1))

# Следующий месяц, плюс одна неделя, в 17:00.
print(dt_now + relativedelta(months=+1, weeks=+1, hour=17))

# Следующая пятница
print(dt_today + relativedelta(weekday=4))

# Узнаем последний вторник месяца
print(dt_today + relativedelta(day=31, weekday=TU(-1)))

# Мы также можем напрямую работать с объектами datetime
# Пример: Определение возраста.

birthday = datetime(1984, 12, 23, 12, 46)
print("Возраст:", relativedelta(dt_now, birthday).years)

# Вывод 5 дней от даты старта
print(
    list(rrule.rrule(rrule.DAILY, count=5, dtstart=parse("20201202T090000"))))


def main():
    # pm()
    # print(get_all_mondays(2023))

    # get_days_in_month(2021, 'December')
    # number_days_one()
    # number_days()
    # day_week()

    # calendar_for_month()

    # leap_year()

    arr = [for_and_append, list_comprehension, list_function]
    # print(get_the_fastest_func(arr, range(100_000)))
    # print(calculate_it(add, 1, 2, 3))
    # fake_news()

    # employees_organization_three()

    # employees_organization_two()

    # employees_organization_one()

    # most_understandable_condition()

    # again_time()

    # get_days_week()

    # sum_data()

    # matem()
    # dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
    # print(fill_up_missing_dates(dates))

    # adjacent_dates()

    # productivity()

    # print(num_of_sundays(768))

    # timer()

    # number_of_seconds()

    # TEST_1:
    dates = ['04.11.2021', '05.11.2021-09.11.2021']
    some_date = '01.11.2021'
    # print(is_available_date(dates, some_date))

    # TEST_2:
    dates = ['04.11.2021', '05.11.2021-09.11.2021']
    some_date = '01.11.2021-04.11.2021'
    # print(is_available_date(dates, some_date))

    # TEST_3:
    dates = ['04.11.2021', '05.11.2021-09.11.2021']
    some_date = '06.11.2021'
    # print(is_available_date(dates, some_date))

    # cosmonaut_diary()

    # fast_code()

    # all_datetime()

    # shop()

    # seconds = 2483228800
    # dt = datetime(2011, 11, 4)
    # print(datetime.fromtimestamp(seconds))
    # print(dt.timestamp())

    # text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в
    # 08:30' dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов
    # принять Вас %d.%m.%Y в %H:%M') print(dt)

    # corrections_data()
    # print(is_correct(31, 12, 2021))
    # print(is_correct(31, 13, 2021))
    dates = [date(1257, 12, 12), date(1992, 6, 23), date(1284, 11, 2),
             date(1992, 1, 1)]
    # print_good_dates(dates)
    # sorting_date()
    # set_two_date()
    # andrew = date(1992, 8, 24) print(andrew.strftime('%Y-%m'))  # выводим
    # дату в формате YYYY-MM print(andrew.strftime('%B(%Y)'))  # выводим
    # дату в формате month_name (YYYY) print(andrew.strftime('%Y-%j'))  #
    # выводим дату в формате YYYY-day_number

    florida_hurricane_dates = [date(2010, 9, 28), date(2017, 1, 13),
                               date(2009, 12, 25),
                               date(2010, 2, 27), date(2021, 10, 11),
                               date(2020, 3, 13),
                               date(2000, 7, 7), date(1999, 4, 14),
                               date(1789, 11, 19),
                               date(2013, 8, 21), date(1666, 6, 6),
                               date(1968, 5, 26)]

    # присваиваем самую раннюю дату урагана в переменную first_date
    # first_date = min(florida_hurricane_dates)

    # конвертируем дату в ISO и RU формат iso = 'Дата первого урагана в ISO
    # формате: ' + first_date.isoformat() ru = 'Дата первого урагана в RU
    # формате: ' + first_date.strftime('%d.%m.%Y') us = 'Дата первого
    # урагана в US формате: ' + first_date.strftime('%m/%d/%Y')
    #
    # print(iso)
    # print(ru)
    # print(us)

    # birthday = date(1992, 10, 6)
    # print('Название месяца:', birthday.strftime('%B'))
    # print('Название дня недели:', birthday.strftime('%A'))
    # print('Год:', birthday.strftime('%Y'))
    # print('Месяц:', birthday.strftime('%m'))
    # print('День:', birthday.strftime('%d'))

    # alarm = time(7, 30, 25)
    # print('Часы:', alarm.strftime('%H'))
    # print('Минуты:', alarm.strftime('%M'))
    # print('Секунды:', alarm.strftime('%S'))

    # date1 = date(2020, 7, 26)
    # date2 = date(2020, 7, 2)
    #
    # print(saturdays_between_two_dates(date1, date2))

    # date1 = date(2021, 10, 1)
    # date2 = date(2021, 10, 5)
    #
    # print(*get_date_range(date1, date2), sep='\n')
    # # print(get_date_range(date1, date2))

    # dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23),
    #          date(1995, 10, 12)]
    # dates = []
    # print(get_min_max(dates))


if __name__ == '__main__':
    main()
