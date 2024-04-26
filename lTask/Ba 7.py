def is_perfect_number(n):
    if n <= 0:
        return False

    divisors_sum = sum(i for i in range(1, n) if n % i == 0)

    return divisors_sum == n
def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Error: Please enter a positive integer.")
        else:
            if is_perfect_number(num):
                print(f"{num} is a perfect number.")
            else:
                print(f"{num} is not a perfect number.")
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()