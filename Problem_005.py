def check(n):
    for i in range(11, 21):
        if n % i == 0:
            continue
        else:
            return False
    return True

x  = 2520

while not check(x):
    x+= 2520

print(x)
