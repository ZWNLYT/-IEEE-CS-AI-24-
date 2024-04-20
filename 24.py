def intersection_area(rect1, rect2):
    x_overlap = max(0, min(rect1[2], rect2[2]) - max(rect1[0], rect2[0]))
    y_overlap = max(0, min(rect1[3], rect2[3]) - max(rect1[1], rect2[1]))
    return x_overlap * y_overlap

t = int(input())
for case in range(1, t + 1):
    n = int(input())
    rectangles = [list(map(int, input().split())) for _ in range(n)]
    common_area = (rectangles[0][2] - rectangles[0][0]) * (rectangles[0][3] - rectangles[0][1])

    for i in range(1, n):
        inter_area = intersection_area(rectangles[i], rectangles[i - 1])
        common_area = min(common_area, inter_area)
    print(f"Case #{case}: {common_area}")
