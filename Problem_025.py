def fib():
    n0 = 1
    n1 = 1
    while True:
        yield n0
        n0, n1 = n1, n0 + n1

index = 1

for f in fib():
    if len(str(f)) >= 1000:
        print(index)
        break
    index += 1
