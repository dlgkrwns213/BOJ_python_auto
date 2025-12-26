import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))

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
            if visited[nxt]:
                continue

            visited[nxt] = True
            q.append(nxt)

    return count


m, n = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

visited = [True if board[i][j] == '.' else False for i in range(n) for j in range(m)]
mx = 0
for idx in range(n*m):
    if not visited[idx]:
        visited[idx] = True
        mx = max(mx, bfs(idx))
print(mx)