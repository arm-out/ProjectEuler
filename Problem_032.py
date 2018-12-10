from itertools import permutations

total = 0

for p in permutations('123456789', 9):
    print(p)
    p = ''.join(p)
    for a in range(3, 4):
        for b in range(5, 6):
            anum = int(p[0:a])
            bnum = int(p[a:b])
            pnum = int(p[b:])
            if anum * bnum == pnum:
                total += pnum

print(total)
