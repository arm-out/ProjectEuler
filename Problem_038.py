def isPandigital(n):
    s = ''.join(str(i) for i in range(1, 10))
    num = str(n)
    if ''.join(sorted(num)) == s:
        return True
    else:
        return False

for n in range(9487, 9213, -1):
    p = str(n * 1) + str(n * 2)
    if isPandigital(p):
        print (p)
