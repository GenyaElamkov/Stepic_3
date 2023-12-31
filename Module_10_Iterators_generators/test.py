import itertools as it
import time


print("Start")
symbols = [".", "-", "'", '"', "'", "-", ".", "_"]

for c in it.cycle(symbols):
    print(c, end="")
    time.sleep(5)
print("End")
