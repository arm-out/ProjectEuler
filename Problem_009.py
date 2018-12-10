x = 1000

for a in range(1, x + 1):
    for b in range(1, x + 1):
        if a > b:
            continue
        c = int((a**2 + b**2)**0.5)
        if a + b + c == x and a**2 + b**2 == c**2:
            print ('a: ' + str(a) +\
                   ' b: ' + str(b) +\
                   ' c: ' + str(c))
            print (a * b * c)
