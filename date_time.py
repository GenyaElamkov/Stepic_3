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


def main():
    date1 = date(2020, 7, 26)
    date2 = date(2020, 7, 2)

    print(saturdays_between_two_dates(date1, date2))


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
