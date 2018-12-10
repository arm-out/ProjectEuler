f = open('names.txt', 'r')
d = f.read()
f.close()

d = d.replace('"', '')
names = d.split(',')
names.sort()

def letterScore(char, _d = {}):
    if char in _d:
        return _d[char]
    _d[char] = ord(char) - ord('A') + 1
    return _d[char]

def alphabeticalValue(name):
    return sum(letterScore(l) for l in name)

def nameScore(name, index):
    return alphabeticalValue(name) * (index + 1);

print (sum(nameScore(names[i], i) for i in range(0, len(names))))
