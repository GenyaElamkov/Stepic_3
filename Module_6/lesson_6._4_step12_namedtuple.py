"""
Выводит фамилии и имена друзей Тимура, предварительно отсортировав их
по дате и времени встречи от самой ранней до самой поздней. Фамилии и имена
должны быть расположены каждые на отдельной строке.

https://stepik.org/lesson/740203/step/12?unit=741843
"""

import csv
from collections import namedtuple
from datetime import datetime


with open('meetings.csv', 'r', encoding='utf-8') as file:
    content = csv.DictReader(file)
    User = namedtuple('User', content.fieldnames)
    users = [User(**k) for k in content]

users_sorted = sorted(sorted(users,
            key=lambda x: datetime.strptime(x.meeting_time, '%H:%M')),
            key=lambda x: datetime.strptime(x.meeting_date, '%d.%m.%Y'))

for k in users_sorted:
    print(k.surname, k.name)
