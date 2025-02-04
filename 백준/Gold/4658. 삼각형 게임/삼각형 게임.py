# https://www.acmicpc.net/problem/4658
import sys
input = sys.stdin.readline
INF = float('inf')


def backtracking(use, bef, minus, tmp):
    global mn
    if use == 63:
        if bef == start:
            mn = min(mn, minus)
        return

    for idx, triangle in enumerate(triangles):
        idx_bit = 1 << idx
        if use & idx_bit:
            continue

        for i in range(3):
            if triangle[i] == bef:
                tmp.append(bef)
                backtracking(use | idx_bit, triangle[i+1], minus + bef, tmp)
                tmp.pop()


ans = []
while True:
    triangles = [list(map(int, input().split())) for _ in range(6)]
    total = sum(map(sum, triangles))
    for triangle in triangles:
        triangle.append(triangle[0])

    mn = INF
    for i in range(3):
        start = triangles[0][i]
        backtracking(1, triangles[0][i+1], start, [start])

    ans.append(str(total - 2 * mn) if mn != INF else 'none')
    if input().rstrip() == '$':
        break

print('\n'.join(ans))