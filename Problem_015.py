def PascalTriangle(n):
    triangle = [[1],
              [1, 1],
    ]
    for n in range(0, n + 1):
        if n == 0 or n == 1:
            continue
        temp_row = []
        for temp in range(1, n + 2):
            temp_row.append(1)
        for i in range(1, n):
            temp_row[i] = triangle[n - 1][i - 1] + triangle[n - 1][i]
        triangle.append(temp_row)
    return triangle

def routes(grid_size):
    number_of_routes = PascalTriangle(grid_size*2)[-1][grid_size]
    return number_of_routes

print (routes(20))
