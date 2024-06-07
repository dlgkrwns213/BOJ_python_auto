# https://www.acmicpc.net/problem/2162
import sys
input = sys.stdin.readline


def ccw(ax, ay, bx, by, cx, cy):
    return (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)


def is_intersect(line1, line2):
    x11, y11, x12, y12 = line1
    x21, y21, x22, y22 = line2
    angle1 = ccw(*line1, x21, y21)
    angle2 = ccw(*line1, x22, y22)
    angle3 = ccw(*line2, x11, y11)
    angle4 = ccw(*line2, x12, y12)

    if not angle1 and min(x11, x12) <= x21 <= max(x11, x12) and min(y11, y12) <= y21 <= max(y11, y12):
        return 1
    if not angle2 and min(x11, x12) <= x22 <= max(x11, x12) and min(y11, y12) <= y22 <= max(y11, y12):
        return 1
    if not angle3 and min(x21, x22) <= x11 <= max(x21, x22) and min(y21, y22) <= y11 <= max(y21, y22):
        return 1
    if not angle4 and min(x21, x22) <= x12 <= max(x21, x22) and min(y21, y22) <= y12 <= max(y21, y22):
        return 1
    return 1 if angle1 * angle2 < 0 and angle3 * angle4 < 0 else 0


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    x = find(a)
    y = find(b)
    if x == y:
        return

    if count[x] > count[y]:
        parent[y] = x
        count[x] += count[y]
        count[y] = 0
    else:
        parent[x] = y
        count[y] += count[x]
        count[x] = 0


n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
intersects = [[0]*n for _ in range(n)]
for i, l1 in enumerate(lines):
    for j, l2 in enumerate(lines[:i]):
        intersects[i][j] = is_intersect(l1, l2)

parent, count = list(range(n)), [1] * n
for i in range(n):
    for j in range(i):
        if intersects[i][j]:
            union(i, j)

print(n - count.count(0))
print(max(count))