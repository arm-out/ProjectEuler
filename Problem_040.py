from operator import mul
from functools import reduce

def product(n):
    return reduce(mul, n, 1)

def findChampernowneIndex(d):
    constant = ""
    for k in range(1, d + 1):
        constant += str(k)
        if len(constant) >= d:
            return int(constant[d-1])

prod = product(findChampernowneIndex(10**x) for x in range(0, 7))
print(prod)
