from collections import deque


def bfs():
    q = deque()
    q.append((1, 0))

    visited = [-1] * (n+1)
    visited[1] = 0
    while q:
        now, cnt = q.popleft()
        if now == n:
            return cnt

        for nxt in (3*now, 2*now, now+1):
            if nxt > n:
                continue
            if visited[nxt] != -1:
                continue

            visited[nxt] = cnt + 1
            q.append((nxt, cnt+1))


n = int(input())
print(bfs())