from num2words import num2words

s = []

for i in range(1, 1001):
    temp = ""
    temp = num2words(i)
    temp = temp.replace("-","")
    temp = temp.replace(" ", "")
    s.append(len(temp))

print (str(sum(s)))
