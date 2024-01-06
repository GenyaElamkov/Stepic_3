"""

https://stepik.org/lesson/674263/step/16?unit=672698
"""

from itertools import combinations

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

res = 0
for i in range(len(wallet)):
    res += sum([sum(n) == 100 for n in set(combinations(wallet, r=i))])

print(res)

if __name__ == "__main__":
    import doctest

    print("\nSTART")
    doctest.testmod()
    print("END")
