# https://www.acmicpc.net/problem/25498
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((1, 1))

    route = [0] * (n+1)
    route[1] = -2

    now_level, last = 0, 1
    while q:
        if now_level != q[0][1]:
            mx = ''
            for node, _ in q:
                for near in graph[node]:
                    if near != route[node]:
                        mx = max(mx, alphabets[near])

            now_level += 1

        now, level = q.popleft()
        last = now
        for nxt in graph[now]:
            if alphabets[nxt] != mx or route[nxt]:
                continue

            route[nxt] = now
            q.append((nxt, level+1))

    ret = []
    while last != 1:
        ret.append(alphabets[last])
        last = route[last]
    ret.append(alphabets[1])
    return ret


n = int(input())
alphabets = ' ' + input().rstrip()
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(''.join(bfs()[::-1]))