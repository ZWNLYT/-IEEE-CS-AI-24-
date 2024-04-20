def convert_to_decimal(N, X):
    decimal = 0
    for digit in N:
        if digit.isdigit():
            value = int(digit)
        else:
            value = ord(digit) - ord('A') + 10
        decimal = decimal * X + value
    return decimal

def convert_to_base(decimal, X):
    result = ''
    while decimal > 0:
        remainder = decimal % X
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        decimal //= X
    return result

T = int(input())
N, X = input().split()

if T == 1:
    decimal = convert_to_decimal(N, int(X))
    print(decimal)
elif T == 2:
    decimal = int(N)
    result = convert_to_base(decimal, int(X))
    print(result)
