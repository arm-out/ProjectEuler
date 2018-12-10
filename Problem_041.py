def isPandigital(n, size):
    s = ''.join(str(i) for i in range(1, size + 1))
    num = str(n)
    if ''.join(sorted(num)) == s:
        return True
    else:
        return False

def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True

n = 7654321
while not (isPandigital(n, 7) and isPrime(n)):
    n -= 2
print(n)
