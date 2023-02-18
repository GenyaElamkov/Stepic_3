"""
Повторяем основы.
"""
from functools import reduce


def hide_card(card_number):
    """
    Реализуйте функцию hide_card(), которая принимает один аргумент:

    card_number — строка, представляющая собой корректный номер банковской
    карты из 16 цифр, между которыми могут присутствовать символы пробела
    Функция должна заменять первые 12 цифр в строке card_number на символ *
    и возвращать полученный результат. Если между цифрами в номере имелись
    символы пробела, их следует удалить.
    """

    return 12 * '*' + card_number.replace(" ", "")[12:]


def same_parity(numbers):
    """
    Реализуйте функцию same_parity(), которая принимает один аргумент:

    numbers — список целых чисел Функция должна возвращать новый список,
    элементами которого являются числа из списка numbers, имеющие ту же
    четность, что и первый элемент этого списка.
    """
    if not numbers:
        return []

    if numbers[0] % 2 == 0:
        return list(filter(lambda x: x % 2 == 0, numbers))
    else:
        return list(filter(lambda x: x % 2 == 1, numbers))

    # return [i for i in nums if i % 2 == nums[0] % 2]


def is_valid(string):
    """
    Будем считать, что PIN-код является корректным, если он удовлетворяет
    следующим условиям:

    состоит из 44, 55 или 66 символов
    состоит только из цифр (0-90−9)
    не содержит пробелов
    Реализуйте функцию is_valid(), которая принимает один аргумент:

    string — произвольная строка Функция должна возвращать значение True,
    если строка string представляет собой корректный PIN-код, или False в
    противном случае.
    """

    # if len(string) < 4 or len(string) > 6:
    #     return False
    return string.isdigit() and len(string) in [4, 5, 6]


def print_given(*args, **kwargs):
    """
    Реализуйте функцию print_given(), которая принимает произвольное
    количество позиционных и именованных аргументов и выводит все переданные
    аргументы, указывая тип каждого. Пары аргумент-тип должны выводиться
    каждая на отдельной строке, в следующем формате:

    для позиционных аргументов:
    <значение аргумента> <тип аргумента>
    для именованных аргументов:
    <имя переменной> <значение аргумента> <тип аргумента>
    """

    [print(c, type(c)) for c in args]
    [print(k, v, type(v)) for k, v in sorted(kwargs.items())]


def convert(text):
    """
    Реализуйте функцию convert(), которая принимает один аргумент:

    string — произвольная строка
    Функция должна возвращать строку string:

    полностью в нижнем регистре, если букв в нижнем регистре в этой строке
    больше полностью в верхнем регистре, если букв в верхнем регистре в этой
    строке больше полностью в нижнем регистре, если количество букв в
    верхнем и нижнем регистрах в этой строке совпадает
    """

    len_upper = sum(list(map(lambda x: x.isupper(), text)))
    len_lower = sum(list(map(lambda x: x.islower(), text)))
    return text.upper() if len_upper > len_lower else text.lower()


def filter_anagrams(word, words):
    """
    Анаграммы — это слова, которые состоят из одинаковых букв. Например:

    адаптер — петарда адресочек — середочка азбука — базука аистенок —
    осетинка Реализуйте функцию filter_anagrams(), которая принимает два
    аргумента в следующем порядке:

    word — слово в нижнем регистре words — список слов в нижнем регистре
    Функция должна возвращать список, элементами которого являются слова из
    списка words, которые представляют анаграмму слова word. Если список
    words пуст или не содержит анаграмм, функция должна вернуть пустой список.
    """

    return [w for w in words if sorted(word) == sorted(w)]
    # return list(filter(lambda x: sorted(word) == sorted(x), words))


def likes(names):
    """
    В различных социальных сетях существуют системы лайков, которые в
    зависимости от количества людей, оценивших запись, показывают
    соответствующую информацию.

    Реализуйте функцию likes(), которая принимает один аргумент:

    names — список имён Функция должна возвращать строку в соответствии с
    примерами ниже, содержание которой зависит от количества имён в списке
    names.
    """
    #
    # if not names:
    #     res = "Никто не оценил данную запись"
    # elif len(names) == 1:
    #     res = f"{names[0]} оценил(а) данную запись"
    # elif len(names) == 2:
    #     res = f"{' и '.join(names)} оценили данную запись"
    # elif len(names) <= 3:
    #     res = f"{names[0]}, {' и '.join(names[1:])} оценили данную запись"
    # else:
    #     res = f"{', '.join(names[:2])} и {len(names) - 2} других оценили " \
    #           f"данную запись "

    match len(names):
        case 0:
            res = "Никто не оценил данную запись"
        case 1:
            res = f"{names[0]} оценил(а) данную запись"
        case 2:
            res = f"{' и '.join(names)} оценили данную запись"
        case 3:
            res = f"{names[0]}, {' и '.join(names[1:])} оценили данную запись"
        case _:
            res = f"{', '.join(names[:2])} и {len(names) - 2} других оценили\
             данную запись "

    return res


def index_of_nearest(numbers, number):
    """
    Реализуйте функцию index_of_nearest(), которая принимает два аргумента в
    следующем порядке:

    numbers — список целых чисел number — целое число Функция должна
    находить в списке numbers ближайшее по значению число к числу number и
    возвращать его индекс. Если список numbers пуст, функция должна вернуть
    число -1.
    """
    if not numbers:
        return -1

    return numbers.index(min(numbers, key=lambda x: abs(x - number)))


def spell(*args):
    """
    Реализуйте функцию spell(), которая принимает произвольное количество
    позиционных аргументов-слов и возвращает словарь, ключи которого —
    первые буквы слов, а значения — максимальные длины слов на эту букву.
    """
    args = [c.lower() for c in args]
    dict_args = dict.fromkeys(map(lambda x: x[0], args))

    for k in dict_args.keys():
        res = list(filter(lambda x: x.startswith(k), args))
        dict_args[k] = len(max(res, key=len))

    return dict_args


def choose_plural(amount, declensions):
    """
    Реализуйте функцию choose_plural(), которая принимает два аргумента в
    следующем порядке:

    amount — натуральное число, количество declensions — кортеж из трех
    вариантов склонения существительного Функция должна возвращать строку,
    полученную путем объединения подходящего существительного из кортежа
    declensions и количества amount, в следующем формате:

    <количество> <существительное>
    один, два, пять
    """

    dic = {0: 2, 1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2,
           11: 2, 12: 2, 13: 2, 14: 2}

    num = int(str(amount)[-2:])
    if num in dic.keys():
        n = num
    else:
        n = amount % 10

    return f"{amount} {declensions[dic[n]]}"


def get_biggest(numbers):
    """
    Реализуйте функцию get_biggest(), которая принимает один аргумент:

    numbers — список целых неотрицательных чисел Функция должна возвращать
    наибольшее число, которое можно составить из чисел из списка numbers.
    Если список numbers пуст, функция должна вернуть число -1.

    Примечание 1. Рассмотрим первый тест со списком чисел [1, 2, 3],
    из которых можно составить следующие числа: 123, 132, 213, 231, 312,
    321 Наибольшим из представленных является 321.
    """

    if not numbers:
        return -1

    tmp = list(map(str, numbers))
    largest = len(max(tmp, key=len))
    sort_largest = sorted(tmp, key=lambda x: x * largest, reverse=True)
    return int("".join(sort_largest))


def track():
    """
    Сегодня Тимур ждёт в гости своего друга Артура, чтобы спланировать
    работу по новому курсу "ООП на Python". Чтобы подготовиться к встрече,
    Тимуру необходимо посетить два магазина, расположенных рядом с его
    домом. От дома до первого магазина ведёт дорожка длиной d_1 метров,
    а до второго магазина ведёт дорожка длиной d_2 метров. Также существует
    дорожка, соединяющая два магазина друг с другом, длиной d_3 метров.
    Напишите программу, которая вычисляет минимальное расстояние, которое
    потребуется пройти Тимуру, чтобы посетить оба магазина и вернуться
    домой. Тимур всегда стартует из дома. Он должен посетить оба магазина,
    перемещаясь только по имеющимся трём дорожкам, и вернуться назад домой.
    При этом его совершенно не смутит, если ему придётся посетить один и тот
    же магазин или пройти по одной и той же дорожке более одного раза.
    Единственная его задача — минимизировать суммарное пройденное расстояние.
    """
    t1, t2, t3 = [int(input()) for _ in range(3)]
    one = t1 + t2 + t3
    two = (t1 + t2) * 2
    three = min((t1 + t3) * 2, (t2 + t3) * 2)

    print(min([one, two, three]))


def similar_letters():
    """
    В русском и английском языках есть буквы, которые выглядят одинаково.
    Вот список английских букв "AaBCcEeHKMOoPpTXxy", а вот их русские
    аналоги "АаВСсЕеНКМОоРрТХху". Напишите программу, которая для трёх букв
    из данных списков букв определяет, русские они, английские или и те и
    другие (смесь русских и английских букв).
    """
    c1, c2, c3 = [input() for _ in range(3)]
    letters = ['m', 't', 'y', 'x', 'a', 'e', 'h', 'o', 'p', 'b', 'k', 'c']
    similar_letters = list(map(lambda x: x.lower() in letters, [c1, c2, c3]))
    match sum(similar_letters):
        case 3:
            res = "en"
        case 0:
            res = "ru"
        case _:
            res = "mix"
    print(res)


def perevorator():
    """
    Дана последовательность натуральных чисел от 1 до nn. Напишите
    программу, которая сначала располагает в обратном порядке часть
    элементов этой последовательности от элемента с номером X до элемента с
    номером Y, а затем от элемента с номером A до элемента с номером B.
    """
    n, a, b, x, y = map(int, input().split())
    n = list(range(1, n + 1))

    n[a - 1:b] = n[a - 1:b][::-1]
    n[x - 1:y] = n[x - 1:y][::-1]
    # nums[x - 1:y] = reversed(nums[x - 1:y])
    # nums[a - 1:b] = reversed(nums[a - 1:b])
    print(*n)


def more_one():
    """
    Дана последовательность неотрицательных целых чисел. Напишите программу,
    которая выводит те числа, которые встречаются в данной последовательности
    более одного раза.
    """
    nums = list(map(int, input().split()))
    res = list(filter(lambda x: nums.count(x) > 1, set(nums)))
    print(*res)


def maximum_group():
    """
    Назовем набор различных натуральных чисел группой. Например: (13, 4, 22,
    40)(13,4,22,40). Тогда длиной группы будем считать количество чисел в
    группе. Например, длина группы (13, 4, 22, 40)(13,4,22,40) равна 44.

    Дана последовательность натуральных чисел от 11 до nn включительно.
    Напишите программу, которая группирует все числа данной
    последовательности по сумме их цифр и определяет длину группы,
    содержащей наибольшее количество чисел.
    """
    arr_nums = list(range(int(input()) + 1))

    res_sum_nums = [sum(map(int, list(str(num)))) for num in arr_nums]
    nums = dict.fromkeys(res_sum_nums, 0)
    for c in res_sum_nums:
        nums[c] += 1
    print(max(nums.values()))


def translation_difficulties():
    """
    Зачастую переводить сериалы, не теряя изначальный смысл, невозможно,
    особенно за счет игр слов. Сумасшедший режиссер хочет снять сериал,
    в котором бы в целях эксперимента задействовал как можно больше языков,
    чтобы пользоваться красотой каждого из них. Тем не менее если
    задействовать слишком много языков, то сериал станет непонятен абсолютно
    всем, поэтому режиссер достает случайных людей на улице и спрашивает их,
    какие языки они знают, таким образом он будет использовать языки которые
    знают все из них.

    Напишите программу, которая определяет, какие языки будут использоваться в
    сериале.
    """

    lines = [input().replace(",", "").split() for _ in range(int(input()))]
    lines = list(map(set, lines))

    result = sorted(reduce(lambda a, b: a.intersection(b), lines))
    if result:
        print(', '.join(result))
    else:
        print("Сериал снять не удастся")


def similar_words():
    """
    Напишите программу, которая находит все схожие слова для заданного
    слова. Слова называются схожими, если имеют одинаковое количество и
    расположение гласных букв. При этом сами гласные могут различаться.
    """

    def set_count_vowel_letters(word: str, letters: list) -> int:
        """
        Возвращает кол-во букв в слове.
        """
        return sum([word.count(c) for c in letters])

    def set_position_vowel_letters(word: str, letters: list) -> list:
        """
        Возвращает расположение букв в слове.
        """
        positions = []
        for i, char in enumerate(word):
            for c in letters:
                if char == c:
                    positions.append(i)
        return positions

    vowel_letters = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]

    # На вход подается слово
    word = input()

    # На входа подается натуральное число - это количество слов для сравнения
    # На вход подаются строки со словами
    words = [input() for _ in range(int(input()))]

    # Отслеживаем текущую гласную букву в входящем слове
    # Проверяем колличесво глассных букв в входящем слове
    count_letters_word = set_count_vowel_letters(word, vowel_letters)
    pos_letters_word = set_position_vowel_letters(word, vowel_letters)

    # Проверяем количество глассных буквы в подающихся строках
    # Если колличество букв во входящем слове одинаково с подающимся строками
    #     выводим подающиеся строку
    for w in words:
        count_letters_w = set_count_vowel_letters(w, vowel_letters)
        pos_letters_w = set_position_vowel_letters(w, vowel_letters)
        if count_letters_word == count_letters_w and pos_letters_word == pos_letters_w:
            print(w)

    # Вариант решения.
    # vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
    # pattern = [i for i, c in enumerate(input()) if c in vowels]
    #
    # for _ in range(int(input())):
    #     word = input()
    #     if [i for i, c in enumerate(word) if c in vowels] == pattern:
    #         print(word)


def main():
    similar_words()
    # translation_difficulties()
    # maximum_group()
    # more_one()
    # perevorator()
    # similar_letters()
    # track() print( get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34,
    # 65, 65, 2, 1])) print(get_biggest([1, 2, 3])) print(get_biggest([61,
    # 228, 9, 3, 11])) print(choose_plural(21, ('пример', 'примера',
    # 'примеров'))) print(choose_plural(92, ('гвоздь', 'гвоздя',
    # 'гвоздей'))) print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
    # print(choose_plural(512312, ('цент', 'цента', 'центов')))

    words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай',
             'УЗБЕКИСТАН']
    words = {}
    # print(spell(*words))
    # print(index_of_nearest([], 17))
    # print(index_of_nearest([7, 13, 3, 5, 18], 0))
    # print(index_of_nearest([9, 5, 3, 2, 11], 4))
    # print(index_of_nearest([7, 5, 4, 4, 3], 4))
    # print(likes([])) print(likes(['Тимур'])) print(likes(['Тимур',
    # 'Артур'])) print(likes(['Тимур', 'Артур', 'Руслан'])) print(likes([
    # 'Тимур', 'Артур', 'Руслан', 'Анри'])) print(likes(['Тимур', 'Артур',
    # 'Руслан', 'Анри', 'Дима'])) print(likes( ['Тимур', 'Артур', 'Руслан',
    # 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))

    # print(filter_anagrams('tommarvoloriddle',
    #                       ['iamlordvoldemort', 'iamdevolremort',
    #                        'mortmortmortmort', 'remortvolremort']))

    # print(convert('pyTHON'))
    # print_given(1, [1, 2, 3], 'three', two=2)
    # print_given('apple', 'cherry', 'watermelon')
    # print_given(b=2, d=4, c=3, a=1)
    # print_given()
    # print(is_valid('121'))
    # print(same_parity([]))
    # card = '3456 9012 5678 1234'
    # card = '1234567890123456'
    # print(hide_card(card))


if __name__ == '__main__':
    main()
