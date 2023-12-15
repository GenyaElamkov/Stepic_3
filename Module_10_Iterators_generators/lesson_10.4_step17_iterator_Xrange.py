"""
Итератор Xrange 🌶️
Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:

start — целое или вещественное число
end — целое или вещественное число
step — целое или вещественное число, по умолчанию имеет значение 
1
1
Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии от start до end, включая start и не включая end, с шагом step, а затем возбуждать исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс Xrange.

https://stepik.org/lesson/669733/step/17?unit=667881
"""


class Xrange:
    def __init__(
        self, start: int | float, end: int | float, step: int | float = 1
    ) -> None:
        self.start = start
        self.end = end
        self.step = step
        self.result = self.start - self.step

    def __iter__(self):
        return self

    def __next__(self) -> int | float:
        self.result += self.step
        
        if (
            self.step > 0
            and (self.result >= self.end)
            or self.step < 0
            and (self.result <= self.end)
        ):
            raise StopIteration
        
        return self.result


evens = Xrange(0, 10, 2)

print(*evens)

xrange = Xrange(0, 3, 0.5)

print(*xrange, sep="; ")

xrange = Xrange(10, 1, -1)

print(*xrange)

xrange = Xrange(5, 10)

print(*xrange)
