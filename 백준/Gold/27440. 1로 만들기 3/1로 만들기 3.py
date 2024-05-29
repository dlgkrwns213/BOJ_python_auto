from collections import deque


def bfs(start):
    q = deque()
    q.append((start, 0))

    visited = set()
    visited.add(start)

    while q:
        now, cnt = q.popleft()
        if now == 1:
            return cnt

        for div in (2, 3):
            nxt = now // div
            if nxt * div != now:
                continue
            if nxt in visited:
                continue

            visited.add(nxt)
            q.append((nxt, cnt+1))

        nxt = now - 1
        if nxt in visited:
            continue

        visited.add(nxt)
        q.append((nxt, cnt + 1))


print(bfs(int(input())))