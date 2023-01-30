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

    return 12*'*' + card_number.replace(" ", "")[12:]


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

def main():
    print(same_parity([]))
    # card = '3456 9012 5678 1234'
    # card = '1234567890123456'
    # print(hide_card(card))


if __name__ == '__main__':
    main()
