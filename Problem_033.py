from fractions import Fraction

product_n = 1
product_d = 1

for n in range(10, 100):
    for d in range(10, 100):
        reduced = n / d
        if reduced >= 1.0:
            continue
        reduced = Fraction(n, d)

        nstr = str(n)
        dstr = str(d)

        for l in nstr:
            if l == '0':
                continue
            if l in dstr:
                rnstr = nstr.replace(l, '')
                rdstr = dstr.replace(l, '')
                if len(rnstr) == 0 or len(rdstr) == 0 or int(rdstr) == 0:
                    continue

                test = Fraction(int(rnstr), int(rdstr))
                if test == reduced:
                    print('%d / %d = %s / %s' % (n, d, rnstr, rdstr))
                    product_n *= int(rnstr)
                    product_d *= int(rdstr)

print(Fraction(product_n, product_d))
