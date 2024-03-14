# https://www.acmicpc.net/problem/12763
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dfs(now, time, money):
    if costs[now]:
        xt, xm = costs[now][0]
        if xt < time and xm < money:
            return
    heappush(costs[now], (money, time))

    if now == n:
        return

    for nxt, nt, nm in graph[now]:
        nxt_time = nt + time
        nxt_money = nm + money
        if nxt_time > mx_time or nxt_money > mx_money:
            continue

        dfs(nxt, nxt_time, nxt_money)


n = int(input())
mx_time, mx_money = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b, t, m = map(int, input().split())
    graph[a].append((b, t, m))
    graph[b].append((a, t, m))


costs = [[] for _ in range(n+1)]
dfs(1, 0, 0)

print(costs[n][0][0] if costs[n] else -1)