def high_and_low(numbers):
    nms = list(map(int, numbers.split()))
    return f"{max(nms)} {min(nms)}"


res = high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
print(res)