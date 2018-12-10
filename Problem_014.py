import functools

@functools.lru_cache(maxsize=None)
def countCollatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        n = n / 2
        return 1 + countCollatz(n)
    n = 3*n + 1
    return 1 + countCollatz(n)

currentMaxCount = 0
for i in range(1, 1000000):
    count = countCollatz(i)
    if count > currentMaxCount:
        currentMaxCount = count
        print (i, count)
