"""
Тимур пришел в книжный магазин, чтобы приобрести новую книгу по математике, стоимость которой равна 
100$. У него в кошельке имеется неограниченное количество купюр, номиналы которых представлены в списке wallet. Другими словами, Тимур может использовать купюру одного номинала произвольное количество раз. Например, он может расплатиться пятью купюрами по 
20$ или десятью по 
10$.

Дополните приведенный ниже код, чтобы он вывел количество способов, которыми Тимур может приобрести книгу стоимостью 
100$.

50,20,20,10 и 
20,10,50,20 считаются одинаковыми и не должны учитываться повторно.

https://stepik.org/lesson/674263/step/16?unit=672698
"""

from itertools import combinations_with_replacement

wallet = [100, 50, 20, 10, 5]


counter = 0
for i in range(21):
    for n in set(combinations_with_replacement(wallet, r=i)):
        if sum(n) == 100:
            counter += 1
print(counter)
    


if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
