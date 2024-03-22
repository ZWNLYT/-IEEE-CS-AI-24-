def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            print("Error: Please enter a positive integer.")
        else:
            result = factorial(num)
            print(f"The factorial of {num} is {result} ({' * '.join(str(i) for i in range(num, 0, -1))}).")
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
