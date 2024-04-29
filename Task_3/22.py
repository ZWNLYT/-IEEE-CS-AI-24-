def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))
def permutation(n, r):
    return factorial(n) / factorial(n-r)
A, B = map(int, input().split())
NCR = combination(A, B)
NPR = permutation(A, B)
print(NCR, NPR)