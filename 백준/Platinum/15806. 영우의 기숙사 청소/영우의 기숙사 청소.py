# https://www.acmicpc.net/problem/15806
import sys
from collections import deque
input = sys.stdin.readline
go = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


def bfs():
    q = deque()
    visited = [[0]*(n+1) for _ in range(n+1)]

    bit = 0
    for x, y in start:
        q.append((x, y, 0))
        visited[x][y] = 1
        bit |= 1 << (x + y) % 2

    finish = n*n if bit == 3 else (n*n // 2)

    day = 0
    nxt = [[0]*(n+1) for _ in range(n+1)]
    while q:
        x, y, d = q.popleft()
        if d == t:
            return nxt

        if d > day:
            # print(d)
            # print(sum(map(sum, visited)), finish)

            if sum(map(sum, visited)) == finish:
                if bit == 3 or (t-d) % 2:
                    return visited
                else:
                    return [[x^1 for x in line] for line in visited]
            # for line in visited[1:]:
            #     print(line[1:])

            visited = nxt
            nxt = [[0]*(n+1) for _ in range(n+1)]
            day += 1

        for a, b in go:
            nx, ny = x+a, y+b
            if nx <= 0 or nx > n or ny <= 0 or ny > n:
                continue
            if nxt[nx][ny]:
                continue

            nxt[nx][ny] = 1
            q.append((nx, ny, d+1))

    return [[0]*(n+1) for _ in range(n+1)]


n, m, k, t = map(int, input().split())
start = [list(map(int, input().split())) for _ in range(m)]

board = bfs()
print('YES' if any(board[line[0]][line[1]] for line in (list(map(int, input().split())) for _ in range(k))) else 'NO')