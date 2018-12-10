def d(n):
    return sum(divisors(n))

def divisors(n):
    return (x for x in range(1, n) if n % x == 0)

def ds(max):
    return [(i, d(i)) for i in range(1, max)]

data = (ds(10000))

numbers = []
for (i, d) in data:
    p = [j for (j, e) in data if e == i and j == d and i != j]
    numbers += p

print(set(numbers))
print(sum(set(numbers)))
