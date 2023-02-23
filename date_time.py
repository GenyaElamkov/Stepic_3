from datetime import date

from math import ceil


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
    # arr = []
    # count_correct_data = 0
    # stop = 'end'
    # while True:
    #     dates = input()
    #     if dates == stop:
    #         print(count_correct_data)
    #         break
    #
    #     day, moth, year = list(map(int, dates.split('.')))
    #
    #     if is_correct(day, moth, year):
    #         count_correct_data += 1
    #         correct_res = "Корректная"
    #     else:
    #         correct_res = "Некорректная"
    #     arr.append(correct_res)
    # print(arr, count_correct_data)
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


def main():
    corrections_data()
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
