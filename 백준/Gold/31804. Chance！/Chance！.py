# https://www.acmicpc.net/problem/31804
from collections import deque
MAX = int(1e6+1)


def bfs() -> int:
    visited = [2] * MAX
    visited[a] = 0

    q = deque()
    q.append((a, 0, 0))

    while q:
        now, count, chance_count = q.popleft()
        if now == b:
            return count

        for nxt in (now+1, 2*now, 10*now):
            if nxt >= MAX:
                continue

            nxt_change_count = chance_count + (1 if nxt == 10 * now else 0)
            if visited[nxt] > nxt_change_count:
                visited[nxt] = nxt_change_count
                q.append((nxt, count+1, nxt_change_count))

    return -1


a, b = map(int, input().split())
print(bfs())