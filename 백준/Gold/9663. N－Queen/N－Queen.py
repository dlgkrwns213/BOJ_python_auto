# https://www.acmicpc.net/problem/9663
def backtracking(row, c_visited, xy_visited, yx_visited):
    global total
    if row == n:
        total += 1
        return

    for col in range(n):
        if c_visited & (1 << col):
            continue

        minus, plus = row - col + n, row + col
        if xy_visited & (1 << minus):
            continue
        if yx_visited & (1 << plus):
            continue

        backtracking(row+1, c_visited | (1 << col), xy_visited | (1 << minus), yx_visited | (1 << plus))


n = int(input())

total = 0
backtracking(0, 0, 0, 0)
print(total)