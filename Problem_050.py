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

max_primes = 500000
primes = []

longest_length = 0
longest_sequence = []
max_sum = 0

for p in prime_gen():
    if p > max_primes:
        break
    primes.append(p)

for i in range(0,len(primes)):
    if i == len(primes) - 1:
        break
    for j in range(i+1, len(primes)):
        if j == len(primes) - 1:
            break
        temp_sum = 0
        temp_primes = []
        for s in range(i, j + 1):
            temp_sum += primes[s]
            temp_primes.append(primes[s])
        if temp_sum > 1000000:
            break
        if isPrime(temp_sum) and j - i + 1 > longest_length:
            longest_length = j - i + 1
            longest_sequence = temp_primes
            max_sum = temp_sum

print(primes)
print(longest_length)
print(longest_sequence)
print(max_sum)
