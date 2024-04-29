def swap_rows(matrix, x, y):
    matrix[x-1], matrix[y-1] = matrix[y-1], matrix[x-1]

def swap_columns(matrix, x, y):
    for i in range(len(matrix)):
        matrix[i][x-1], matrix[i][y-1] = matrix[i][y-1], matrix[i][x-1]

def print_matrix(matrix):
    for row in matrix:
        print(*row)

N, X, Y = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

swap_rows(matrix, X, Y)
swap_columns(matrix, X, Y)

print_matrix(matrix)
