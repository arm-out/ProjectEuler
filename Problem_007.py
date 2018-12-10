def isPrime(n):
    if n % 2 == 0:
        return False
    p = 3
    while p < (n ** 0.5) + 1:
        if n % p == 0:
            return False
        p += 2
    return True

def nthPrime(nth):
    prime = 2
    count = 1
    iter = 3
    while count < nth:
        if isPrime(iter):
            count += 1
            prime = iter
        iter += 2
    return prime

print (nthPrime(10001))
