def isPrime(n, cache = {2: True}):
    if n in cache:
        return cache[n]

    if n % 2 == 0:
        cache[n] = False
        return False
    p = 3
    while p < (n ** 0.5) + 1:
        if n % p == 0:
            cache[n] = False
            return False
        p += 2
    cache[n] = True
    return True

def prime_gen():
    yield 2
    n = 3
    while True:
        yield n
        n += 2
        while not isPrime(n):
            n += 2

def prime_factors(n):

    factors = []
    for p in prime_gen():
        if p <= n and n % p == 0:
            factors.append(p)
        if p > n:
            break
    return factors

a = 100000
b = a + 1
c = a + 2
d = a + 3

while True:
    if len(prime_factors(a)) == 4 and len(prime_factors(b)) == 4 and len(prime_factors(c)) == 4 and len(prime_factors(d)) == 4:
        print(a, b, c, d)
        break
    else:
        a += 1
