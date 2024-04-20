def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
A, B = map(int, input().split())
print(gcd(A, B), lcm(A, B))