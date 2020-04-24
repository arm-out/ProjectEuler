# nk+1 = nk + 2dk
# dk+1 = nK+1 - dk

n_greator = 0

numer = 3
denom = 2

for i in range(1000):
    numer += 2 * denom
    denom = numer - denom

    if (len(str(numer)) > len(str(denom))):
        n_greator += 1

print(n_greator)
