def minimize_number(n, arr):
    operations = 0
    while all(num % 2 == 0 for num in arr):
        operations += 1
        arr = [num // 2 for num in arr]
    return operations

n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

if len(arr) != n:
    print("Invalid input")
else:
    result = minimize_number(n, arr)
    print(f"The maximum number of operations that can be performed is: {result}")