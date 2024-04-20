def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a number greater than 0."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a number N (1 ≤ N ≤ 30): "))

if 1 <= n <= 30:
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
else:
    print("Invalid input. Please enter a number within the valid range (1 ≤ N ≤ 30).")