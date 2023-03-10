from datetime import date
from datetime import datetime
from datetime import time
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

    with open("diary.txt", "r", encoding="utf-8") as f:
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


def main():
    dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
    print(fill_up_missing_dates(dates))

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
