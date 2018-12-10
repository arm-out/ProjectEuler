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

def rotations(num):
    def rotate(s, n):
        return s[n:] + s[:n]
    rots = []
    for i in range(0, len(num)):
        rots.append(rotate(num, i))
    return rots

def isCircularPrime(n):
    s = str(n)
    rots = rotations(s)
    for p in rots:
        if not isPrime(int(p)):
            return False
    return True

circular_primes = []

for i in range(2, 1000000):
    if isPrime(i) and isCircularPrime(i):
        circular_primes.append(i)

print(len(circular_primes))
