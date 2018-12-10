def isPalindrome(n):
    s = str(n)
    for n in range(1, int(len(s)/2) + 1):
        if s[n-1] != s[-n]:
            return False
    return True

def decimalToBinary(n):
    return int(bin(n)[2:])

total = 0

for i in range(1, 1000000):
    if isPalindrome(i) and isPalindrome(decimalToBinary(i)):
        total += i

print(total)
