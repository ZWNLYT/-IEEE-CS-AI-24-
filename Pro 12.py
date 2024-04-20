def replace_minmax(arr):
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))
    arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
    return arr

N = int(input("Enter the number of elements: "))

if N < 2 or N > 1000:
    print("Invalid number of elements. Please enter a number between 2 and 1000.")
    exit()

print("Enter the array elements:")
arr = list(map(int, input().split()))

if len(arr) != N:
    print("Invalid number of elements provided. Please enter exactly", N, "elements.")
    exit()

result = replace_minmax(arr)
print("The modified array is:")
print(*result)