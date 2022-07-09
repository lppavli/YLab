import math


def zeros(n):
    if n == 0:
        return 0
    summ = 0
    for i in range(1, int(math.log(n, 5)) + 1):
        summ += n // (5**i)
    return summ


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
