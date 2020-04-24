def isPalindrome(n):
    s = str(n)
    for n in range(1, int(len(s)/2) + 1):
        if s[n-1] != s[-n]:
            return False
    return True

def reverseNum(n):
    s = str(n)
    newNum = ""

    for i in range(len(s)):
        newNum += s[len(s)-1-i]

    return int(newNum)

lychrelNums = 0

for i in range(1, 10000):
    iterations = 0
    sum = 0
    num = i

    while True:
        sum = num + reverseNum(num)
        iterations += 1
        if (isPalindrome(sum)):
            break
        elif (not (isPalindrome(sum)) and iterations > 50):
            lychrelNums += 1
            break
        else:
            num = sum

print (lychrelNums)


