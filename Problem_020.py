def factorial(n):
    total = 1
    while n != 1:
        total *= n
        n -= 1
    return str(total)

def sumOfDigits(n):
    result = 0
    for i in range(0, len(factorial(n))):
        result += int(factorial(n)[i])
    return result

print (sumOfDigits(100))
