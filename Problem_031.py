#1p, 2p, 5p, 10p, 20p, 50p, lb1 (100p) and lb2 (200p)

solutions = []

def checkSum(pound2, pound1, pence50, pence20, pence10, pence5, pence2, pence1):
    s = sum([
        pound2 * 200,
        pound1 * 100,
        pence50 * 50,
        pence20 * 20,
        pence10 * 10,
        pence5 * 5,
        pence2 * 2,
        pence1 * 1
    ])
    return s

def checkCoins(pound2, pound1, pence50, pence20, pence10, pence5, pence2, pence1):
    s = sum([
        pound2 * 200,
        pound1 * 100,
        pence50 * 50,
        pence20 * 20,
        pence10 * 10,
        pence5 * 5,
        pence2 * 2,
        pence1 * 1
    ])
    return s == 200, 'lb2 %d, lb1 %d, 50p %d, 20p %d, 10p %d, 5p %d, 2p %d, 1p %d' % (pound2, pound1, pence50, pence20, pence10, pence5, pence2, pence1)

for pound2 in range(0, 1 + 1):
    for pound1 in range(0, 2 + 1):
        if checkSum(pound2, pound1, 0, 0, 0, 0, 0, 0) > 200:
            continue
        for pence50 in range(0, 4 + 1):
            if checkSum(pound2, pound1, pence50, 0, 0, 0, 0, 0) > 200:
                continue
            for pence20 in range(0, 10 + 1):
                if checkSum(pound2, pound1, pence50, pence20, 0, 0, 0, 0) > 200:
                    continue
                for pence10 in range(0, 20 + 1):
                    if checkSum(pound2, pound1, pence50, pence20, pence10, 0, 0, 0) > 200:
                        continue
                    for pence5 in range(0, 40 + 1):
                        if checkSum(pound2, pound1, pence50, pence20, pence10, pence5, 0, 0) > 200:
                            continue
                        for pence2 in range(0, 100 + 1):
                            if checkSum(pound2, pound1, pence50, pence20, pence10, pence5, pence2, 0) > 200:
                                continue
                            for pence1 in range(0, 200 + 1):
                                success, combo = checkCoins(pound2,
                                                            pound1,
                                                            pence50,
                                                            pence20,
                                                            pence10,
                                                            pence5,
                                                            pence2,
                                                            pence1)
                                if success :
                                    solutions.append(combo)

print (solutions)
print (len(solutions))
