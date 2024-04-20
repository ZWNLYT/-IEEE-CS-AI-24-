def check_code(A, B, c):
    if len(c) != A + B + 1:
        return "No"
    if c[A] != '-':
        return "No"

    for i in range(len(c)):
        if i != A and not c[i].isdigit():
            return "No"

    return "Yes"

A, B = map(int, input().split())

c = input()
result = check_code(A, B, c)

print(result)
