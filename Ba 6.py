def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return factors

def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Error: Please enter a positive integer.")
        else:
            factors = prime_factors(num)
            if len(factors) == 0:
                print("The number is prime.")
            else:
                print(f"The prime factors of {num} are: {', '.join(map(str, factors))}")
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
