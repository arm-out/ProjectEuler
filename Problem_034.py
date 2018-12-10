from math import factorial

curious_numbers = []

for i in range(3, 100000):
    s = sum(factorial(int(l)) for l in str(i))
    if s == i:
        curious_numbers.append(i)
        print(i, sum(curious_numbers))
