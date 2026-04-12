# https://www.acmicpc.net/problem/30396
from collections import deque
go = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))


def bfs():
    visited = [False] * (1 << 16)
    visited[start] = True

    q = deque()
    q.append((start, 0))

    while q:
        now, cnt = q.popleft()
        if now == destination:
            return cnt

        for move in range(16):
            move_bit = 1 << move
            if not now & move_bit:
                continue

            nxt = now & ~move_bit
            x, y = divmod(move, 4)
            for a, b in go:
                nx, ny = x+a, y+b
                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                    continue

                nxt_add_bit = 1 << (4 * nx + ny)
                if nxt & nxt_add_bit:
                    continue

                added_nxt = nxt | nxt_add_bit
                if visited[added_nxt]:
                    continue

                visited[added_nxt] = True
                q.append((added_nxt, cnt+1))

    return -1


start = int(''.join(input() for _ in range(4)), 2)
destination = int(''.join(input() for _ in range(4)), 2)

print(bfs())