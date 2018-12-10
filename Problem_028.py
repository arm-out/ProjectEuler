def oddNumbers(max):
    n = 1
    while n <= max:
        yield n
        n += 2

def getLayers(size):
    layers = len(list(oddNumbers(size))) - 1
    return layers

top_right = []
top_left = []
bottom_right = []
bottom_left = []

def topLeft(n):
    return 4*(n**2) - 6*n + 3

def topRight(n):
    return 4*(n**2) - 4*n + 1

def bottomLeft(n):
    return 4*(n**2) - 8*n + 5

def bottomRight(n):
    return 4*(n**2) - 10*n + 7

def sumOfDiag(size):
    for n in range(2, getLayers(size) + 2):
        top_left.append(topLeft(n))
        top_right.append(topRight(n))
        bottom_right.append(bottomRight(n))
        bottom_left.append(bottomLeft(n))
    diag_up = bottom_left + top_right
    diag_down = top_left + bottom_right
    diagonals = diag_up + diag_down
    diagonals.append(1)
    return sum(diagonals)

print (sumOfDiag(1001))
