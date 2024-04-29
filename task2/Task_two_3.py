if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))
    unique_sorted_arr = sorted(set(arr), reverse=True)
    print(unique_sorted_arr[1])
