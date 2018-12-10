def isPrime(n):
    if n % 2 == 0:
        return False
    p = 3
    while p < (n ** 0.5) + 1:
        if n % p == 0:
            return False
        p += 2
    return True

def sumOfPrimes(max):
    total = 2
    iter = 3
    while iter < max:
        if isPrime(iter):
            total += iter
        iter += 2
    return total

print (sumOfPrimes(2000000))
