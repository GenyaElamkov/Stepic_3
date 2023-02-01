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

    # return [w for w in words if sorted(word) == sorted(w)]
    return list(filter(lambda x: sorted(word) == sorted(x), words))


def main():
    print(filter_anagrams('tommarvoloriddle',
                          ['iamlordvoldemort', 'iamdevolremort',
                           'mortmortmortmort', 'remortvolremort']))

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
