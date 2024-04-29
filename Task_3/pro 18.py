def xor_operation(a, b, q):
    result = a
    for _ in range(q - 1):
        result = result ^ b
    return result

a, b, q = map(int, input().split())

print(xor_operation(a, b, q))