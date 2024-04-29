
def smallest_pair(arr):
    min_sum = float('inf')

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            curr_sum = arr[i] + arr[j] + j - i

            min_sum = min(min_sum, curr_sum)

    return min_sum

t = int(input())

for _ in range(t):

    n = int(input())
    arr = list(map(int, input().split()))
    result = smallest_pair(arr)
    print(result)
