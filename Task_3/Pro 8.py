def max_path_sum(matrix, i, j, n, m):
    if i == n or j == m:
        return 0
    return max(matrix[i][j] + max_path_sum(matrix, i + 1, j, n, m),
               matrix[i][j] + max_path_sum(matrix, i, j + 1, n, m))
def main():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(max_path_sum(matrix, 0, 0, n, m))

if __name__ == "__main__":
    main()