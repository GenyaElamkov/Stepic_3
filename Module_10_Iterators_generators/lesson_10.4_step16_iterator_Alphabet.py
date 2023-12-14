"""
Итератор Alphabet 🌶️
Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:

language — код языка: ru — русский, en — английский
Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:

русского алфавита, если language имеет значение ru
английского алфавита, если language имеет значение en
Примечание 1. Буква ё в русском алфавите не учитывается.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Alphabet.

https://stepik.org/lesson/669733/step/16?unit=667881
"""


class Alphabet:
    def __init__(self, language: str) -> None:
        self.language = language
        self.counter = -1
        self.lang = {
            "en": {"start": 97, "stop": 122},
            "ru": {"start": 1072, "stop": 1103},
        }

    def __iter__(self):
        return self

    def __next__(self) -> str:
        self.counter += 1
        res = self.lang[self.language]["start"] + self.counter
        if res == self.lang[self.language]["stop"]:
            self.counter = -1

        return chr(res)


en_alpha = Alphabet("en")

letters = [next(en_alpha) for _ in range(28)]

print(*letters)
