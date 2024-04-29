def max_subarray(arr):
    result = []
    for i in range(len(arr)):
        max_num = float('-inf')
        for j in range(i, len(arr)):
            max_num = max(max_num, arr[j])
            result.append(max_num)
    return result

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    result = max_subarray(arr)

    print(*result)


