# https://www.acmicpc.net/problem/4994
import sys
from collections import deque
input = sys.stdin.readline


def bfs(num):
    q = deque()
    q.append((1, '1'))

    visited = [0] * (num+1)
    visited[1] = 1

    while True:
        now, real = q.popleft()
        if now in (0, num):
            return real

        ten = now * 10 % num
        nxt_reals = (real+'0', real+'1')
        for idx, nxt in enumerate((ten, ten+1)):
            if visited[nxt]:
                continue

            visited[nxt] = 1
            q.append((nxt, nxt_reals[idx]))


ans = []
while True:
    n = int(input())
    if not n:
        break

    ans.append(bfs(n))

print('\n'.join(map(str, ans)))