RA, CA = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(RA)]
RB, CB = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(RB)]

C = [[0] * CB for _ in range(RA)]
for i in range(RA):
    for j in range(CB):
        for k in range(CA):
            C[i][j] += A[i][k] * B[k][j]
for row in C:
    print(*row)
