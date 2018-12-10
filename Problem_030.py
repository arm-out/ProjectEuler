narcissistic = []

upper_bound = 1 + sum(x**5 for x in range(1, 11))

for i in range(2, upper_bound):
    numstring = str(i)
    total = 0
    for num in numstring:
        numint = int(num)
        total += numint**5
    if total == i:
        narcissistic.append(i)

print(sum(narcissistic))
