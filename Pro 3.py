def print_digits_recursive(n):
    if n == 0:
        return
    else:
        print_digits_recursive(n // 10)
        print(n % 10, end=' ')

T = int(input())
numbers = []
for i in range(T):
    numbers.append(int(input()))

for num in numbers:
    print_digits_recursive(num)
    print()
