import sys
from collections import deque
input = sys.stdin.readline
go = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j]


def bfs(start):
    q = deque()
    q.append(start)

    count = 0
    while q:
        now = q.popleft()
        x, y = divmod(now, m)
        count += 1

        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            nxt = nx * m + ny
            if board[nxt] != '.' or visited[nxt]:
                continue

            visited[nxt] = True
            q.append(nxt)

    return count


m, n = map(int, input().split())
board = ''.join(input().rstrip() for _ in range(n))

visited = [0] * (n*m)
answer = 0
for idx in range(n*m):
    if board[idx] == '.' and not visited[idx]:
        visited[idx] = True
        answer = max(answer, bfs(idx))

print(answer)