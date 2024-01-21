"""
Социальные сети
Вам доступен набор популярных публикаций из социальной сети Твиттер, которые могут иметь следующий вид:

Люблю курсы BEEGEEK!
Когда курс по ООП? @timur_guev
BEEGEEK, спасибо за курсы, вы лучшие! #python #BeeGeek
и т.д.
Напишите программу, которая определяет, в скольких публикациях содержится строка beegeek.

Формат входных данных
На вход программе подается произвольное число строк, каждая из которых представляет очередную публикацию.

Формат выходных данных
Программа должна определить, в скольких введенных строках содержится строка beegeek в произвольном регистре, и вывести полученный результат.

https://stepik.org/lesson/640164/step/6?unit=636683
"""

import re

article = """Stepik (до августа 2016 года Stepic) — это образовательная платформа и конструктор онлайн-курсов!

Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android. В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном режиме для iOS и Android...

На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
Stepik позволяет любому зарегистрированному пользователю создавать интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и разнообразные задачи с автоматической проверкой и моментальной обратной связью. 

Проект сотрудничает как с образовательными учреждениями, так и c индивидуальными преподавателями и авторами.  
Stepik сегодня предлагает онлайн-курсы от образовательных организаций, а также индивидуальных авторов!

Система автоматизированной проверки задач Stepik была использована в ряде курсов на платформе Coursera, включая курсы по биоинформатике от Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ «Высшая школа экономики»...

Stepik также может функционировать как площадка для проведения конкурсов и олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ (2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант в 2017 году, соревнования по информационной безопасности StepCTF-2015..."""

pattern_start = r"^(Stepik)"
pattern_end = r"([.]{3}|!)$"
match_start = re.finditer(pattern_start, article, flags=re.I|re.M)
match_end = re.finditer(pattern_end, article, flags=re.I|re.M)
print(len(list(match_start)), len(list(match_end)), sep="\n")