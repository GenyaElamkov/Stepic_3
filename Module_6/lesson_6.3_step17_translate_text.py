"""
Напишите программу, которая с помощью данной строки переводит заданный текст.

https://stepik.org/lesson/631917/step/17?unit=627943
"""

from string import ascii_uppercase


def main():
    d = dict(zip(ascii_uppercase, input()))
    text = ''.join(map(lambda x: x.upper(), input()))
    translate_text = text.translate(text.maketrans(d))
    print(translate_text)


if __name__ == '__main__':
    main()
