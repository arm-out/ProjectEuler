def sumOfSquares(limit):
    total = 0
    for i in range(1, limit + 1):
        total += i ** 2
    return total

def squareOfSum(limit):
    total = 0
    for i in range(1, limit + 1):
        total += i
    return total ** 2

s1 = sumOfSquares(100)
s2 = squareOfSum(100)

print(s2 - s1)
