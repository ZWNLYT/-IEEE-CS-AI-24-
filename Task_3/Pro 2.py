def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n)

n = int(input("Enter a number: "))
print_numbers(n)