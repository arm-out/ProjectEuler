def isPalindrome(n):
    s = str(n)
    for n in range(1, int(len(s)/2) + 1):
        if s[n-1] != s[-n]:
            return False
    return True

largestPalindrome = 0

for j in range(100, 1000):
    for k in range(j, 1000):
        if isPalindrome(j*k):
            if (j*k) > largestPalindrome:
                largestPalindrome = j*k

print (largestPalindrome)
