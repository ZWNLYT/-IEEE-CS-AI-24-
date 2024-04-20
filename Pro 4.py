def array_average(arr, n):
    if n == 0:
        return 0
    else:
        return (arr[n - 1] + array_average(arr, n - 1))

def calculate_average(arr, n):

    sum_of_elements = array_average(arr, n)

    average = sum_of_elements / n

    return round(average, 6)
n = int(input())

arr = list(map(int, input().split()))

average = calculate_average(arr, n)

print(average)