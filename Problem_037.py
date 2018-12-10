def isPrime(n, cache = {2: True}):
    if n in cache:
        return cache[n]

    if n == 1:
        cache[1] = False
        return False

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

def truncateLeft(n):
    sl = str(n)
    intsl = []
    for i in range(1, len(sl)):
        intsl.append(int(sl[i:]))
    return intsl

def truncateRight(n):
    sr = str(n)
    intsr = []
    for i in range(len(sr) - 1, 0, -1):
        intsr.append(int(sr[:i]))
    return intsr

def checkTruncates(n):
    left_truncates = truncateLeft(n)
    right_truncates = truncateRight(n)
    for i in range(0, len(left_truncates)):
        tempr = right_truncates[i]
        templ = left_truncates[i]
        if not isPrime(tempr) or not isPrime(templ):
            return False
    return True

total = 0

for i in range(10, 800000):
    if isPrime(i) and checkTruncates(i):
        total += i

print(total)
