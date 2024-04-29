def is_permutation(n, a, b):
    return sorted(a) == sorted(b)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if is_permutation(n, a, b):
    print("yes")
else:
    print("no")