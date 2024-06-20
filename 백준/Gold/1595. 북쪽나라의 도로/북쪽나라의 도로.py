# https://www.acmicpc.net/problem/1595
import sys
input = sys.stdin.readline


def dfs(now, bef):
    node, mx_dist = now, 0
    for nxt, weight in graph[now]:
        if bef == nxt:
            continue

        nxt_node, nxt_dist = dfs(nxt, now)
        if mx_dist < nxt_dist + weight:
            mx_dist = nxt_dist + weight
            node = nxt_node

    return node, mx_dist


graph = [[] for _ in range(10001)]
ipt = False
while True:
    try:
        u, v, w = map(int, input().split())
        ipt = True
    except ValueError or EOFError:
        break
    graph[u].append((v, w))
    graph[v].append((u, w))

if ipt:
    a, _ = dfs(u, -1)
    _, d = dfs(a, -1)
    print(d)
else:
    print(0)