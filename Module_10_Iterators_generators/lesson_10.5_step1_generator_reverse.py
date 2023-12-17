"""
Функция reverse()
Реализуйте генераторную функцию reverse(), которая принимает один аргумент:

sequence — последовательность
Функция должна возвращать генератор, порождающий элементы последовательности sequence в обратном порядке, а затем возбуждающий исключение StopIteration.

Примечание 1. Последовательностью является коллекция, поддерживающая индексацию и имеющая длину. Например, объекты типа list, str, tuple являются последовательностями.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию reverse(), но не код, вызывающий ее.


https://stepik.org/lesson/640048/step/18?unit=636568
"""

def reverse(sequence):
    for i in sequence[::-1]:
        yield i


generator = reverse('beegeek')

print(type(generator))
print(*generator)