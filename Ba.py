def find_largest_smallest():
    largest = None
    smallest = None

    while True:
        num = int(input("Enter a number (-1 to stop): "))

        if num == -1:
            break

        if largest is None:
            largest = num
            smallest = num
        else:
            if num > largest:
                largest = num
            elif num < smallest:
                smallest = num

    print(f"Largest number: {largest}")
    print(f"Smallest number: {smallest}")

find_largest_smallest()