"""
Итератор Cycle
Реализуйте класс Cycle, порождающий итераторы, конструктор которого принимает один аргумент:

iterable — итерируемый объект
Итератор класса Cycle должен циклично генерировать последовательность элементов итерируемого объекта iterable.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в конструктор класса, не является множеством и итератором.

Примечание 2. Элементы итерируемого объекта, генерируемые итератором, должны располагаться в своем изначальном порядке.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый класс Cycle.

https://stepik.org/lesson/669733/step/14?unit=667881
"""


class Cycle:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if len(self.iterable) == self.counter:
            self.counter = 0
        return self.iterable[self.counter]


cycle = Cycle(range(100_000_000))

print(next(cycle))
print(next(cycle))
