from math import factorial


def zeros(n):
    res = factorial(n)
    count = 0
    while res % 10 == 0:
        count += 1
        res //= 10
    return count


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
