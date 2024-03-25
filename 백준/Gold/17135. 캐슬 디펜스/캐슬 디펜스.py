# https://www.acmicpc.net/problem/17135
import sys
input = sys.stdin.readline


# 현재 위치에서 타겟 우선순위 정하기
def get_target_priority(x, y):
    for i in range(d):
        for j in range(-i, i+1):
            nx, ny = x-1-i+abs(j), y+j
            if nx < 0 or ny < 0 or ny >= m:
                continue
            if board[nx][ny]:
                return nx, ny
    return -1, -1


# 궁수 위치가 정해졌을 경우 시뮬레이션
def simulation(loc):
    total, tmp = 0, []
    for x in range(n, 0, -1):
        eliminate = set()
        for y in loc:
            ex, ey = get_target_priority(x, y)
            if ex == -1:
                continue

            eliminate.add((ex, ey))

        for ex, ey in eliminate:
            board[ex][ey] = 0
            total += 1
            tmp.append((ex, ey))

    for x, y in tmp:
        board[x][y] = 1

    return total


# 궁수 위치 정하기
def backtracking(cnt, idx, loc):
    global mtotal
    if cnt == 3:
        mtotal = max(mtotal, simulation(loc))
        return

    for i in range(idx, m):
        loc.append(i)
        backtracking(cnt+1, i+1, loc)
        loc.pop()


n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

mtotal = 0
backtracking(0, 0, [])
print(mtotal)
