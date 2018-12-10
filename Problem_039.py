limit = 1000
t_max = 0
p_max = 0

for p in range(limit//4*2, limit + 1, 2):
    t = 0
    for a in range(2, int(p/3.4142) + 1):
        if p*(p - 2*a) % (2*(p - a)) == 0:
            t += 1
            if t >= t_max:
                t_max = t
                p_max = p

print(p_max)
