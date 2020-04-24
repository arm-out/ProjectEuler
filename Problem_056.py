def sumOfDigits(n):
    sum = 0

    for i in range(len(str(n))):
        sum += int(str(n)[i])
    
    return sum

maxSum = 0

for a in range(100):
    for b in range(100):
        num = a**b

        if (sumOfDigits(num) > maxSum):
            maxSum = sumOfDigits(num)

print (maxSum)
