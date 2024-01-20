def last_digit(n1, n2):
    if n2 == 0:
        return 0
    elif n2 == 1:
        return n1 % 10
    elif n2 % 2 != 0:
        return n1 * last_digit(n1, n2 - 1) % 10
    elif n2 % 2 == 0:
        return last_digit(n1 * n1, n2 / 2) % 10
    


# print(last_digit(2**200, 2**300))
print(last_digit(4, 2))
