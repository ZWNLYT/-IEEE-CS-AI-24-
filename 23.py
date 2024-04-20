import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

radius_A = distance(x1, y1, x2, y2) / 2
radius_B = distance(x3, y3, x4, y4) / 2
center_distance = distance((x1 + x2) / 2, (y1 + y2) / 2, (x3 + x4) / 2, (y3 + y4) / 2)

if center_distance <= radius_A + radius_B:
    print("YES")
else:
    print("NO")
