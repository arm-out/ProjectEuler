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

def quadraticPrimes(a, b):
    n = 0
    q = abs(n**2 + a*n + b)
    p = isPrime(q)
    while p:
        yield q
        n += 1
        q = abs(n**2 + a*n + b)
        p = isPrime(q)

#current_longest = (1, 41, len(list(quadraticPrimes(1, 41))))
current_longest = (0, 0, 0)
for a in range(-999, 1000):
    if not isPrime(abs(a)):
        continue
    for b in range(-1000, 1001):
        if not isPrime(abs(b)):
            continue
        primes = list(quadraticPrimes(a, b))
        if len(primes) > current_longest[2]:
            current_longest = (a, b, len(primes))

print(current_longest)
print(current_longest[0] * current_longest[1])
