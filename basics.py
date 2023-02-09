"""
Повторяем основы.
"""


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
            res = f"{', '.join(names[:2])} и {len(names) - 2} других оценили данную запись "

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
    n = amount % 10
    dic = {0: 2, 1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}
    return f"{amount} {declensions[dic[n]]}"


def main():
    print(choose_plural(21, ('пример', 'примера', 'примеров')))
    print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
    print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
    print(choose_plural(512312, ('цент', 'цента', 'центов')))

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
