"""
Вам доступен именованный кортеж User, который содержит данные о пользователе
 некоторого ресурса. Первым элементом именованного кортежа является имя
 пользователя, вторым — фамилия, третьим — адрес электронной почты,
 четвертым — статус оформленной подписки. Также доступен список users,
 содержащий эти кортежи.

Дополните приведенный ниже код, чтобы он вывел данные о каждом пользователе
из этого списка, предварительно отсортировав их по статусу подписки от
дорогой к дешевой, а при совпадении статусов — в лексикографическом порядке
адресов электронных почт. Данные о каждом пользователе должны быть указаны
 в следующем формате:

<имя> <фамилия>
  Email: <адрес электронной почты>
  Plan: <статус подписки>

https://stepik.org/lesson/740203/step/11?unit=741843
"""

from collections import namedtuple

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

users_sorted = sorted(users, key=lambda x: (('Gold', 'Silver', 'Bronze', 'Basic').index(x.plan), x.email))

for user in users_sorted:
    print(f"""
{user.name} {user.surname}
  Email: {user.email}
  Plan: {user.plan}""")

# Вариант решения.
# status = {'Gold': 0, 'Silver': 1, 'Bronze': 2, 'Basic': 3}
# for user in sorted(users, key=lambda x: (status[x.plan], x.email)):
#     print('{0} {1}\n  Email: {2}\n  Plan: {3}\n'.format(*user))