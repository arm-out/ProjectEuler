from itertools import permutations, combinations
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

primes = prime_gen()
p = next(primes)
four_digit_primes = set()

while len(str(p)) <= 4:
    p = next(primes)
    if len(str(p)) == 4:
        four_digit_primes.add(p)

permutation_list = []

for prime in four_digit_primes:
    possibles = permutations(str(prime), 4)
    temp_perms = []
    for possible in possibles:
        q = int(''.join(possible))
        if q in four_digit_primes and q not in temp_perms:
            temp_perms.append(q)
    permutation_list.append(temp_perms)

arithmetic_primes = []

for i in permutation_list:
    if len(i) <= 2:
        continue
    for subset in combinations(i, 3):
        s = sorted(subset)
        if s[1] - s[0] == s[2] - s[1] and s not in arithmetic_primes:
            arithmetic_primes.append(s)

for i in arithmetic_primes:
    concatenation = ''
    for k in i:
        concatenation = concatenation + str(k)
    print(concatenation)
