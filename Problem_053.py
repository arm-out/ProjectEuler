import math

n = 23
r = 10
counter = 0
done = False

def Combination(n, r):
    ans = (math.factorial(n)) / (math.factorial(r) * math.factorial(n - r))
    return ans

while not done and n <= 100:
    while r < n:
        if Combination(n, r) > 1000000:
            counter += 1
        r += 1
    n += 1
    r = 1

print(counter)
