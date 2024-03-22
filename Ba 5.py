def sum_of_even_numbers(n):
    return sum(i for i in range(2, n + 1, 2))

def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Error: Please enter a positive integer.")
        else:
            result = sum_of_even_numbers(num)
            print(f"The sum of even numbers from 1 to {num} is {result}"
                  f" ({' + '.join(str(i) for i in range(2, num + 1, 2))}).")
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
