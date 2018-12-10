from math import sqrt

def isTriangleNumber(n):
    return not bool(((sqrt(1 + 8*n) - 1) / 2) % 1)

def score(word):
    return sum(abs(64 - ord(letter)) for letter in word)

words = [x[1:-1] for x in open('words.txt').read().split(',')]
print(sum(isTriangleNumber(score(word)) for word in words))
