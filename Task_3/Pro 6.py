def can_reach(current_value, target_value):
    if current_value == target_value:
        return True

    if current_value > target_value:
        return False

    return can_reach(current_value * 10, target_value) or can_reach(current_value * 20, target_value)

T = int(input())

for _ in range(T):

    N = int(input())

    if can_reach(1, N):
        print("YES")
    else:
        print("NO")