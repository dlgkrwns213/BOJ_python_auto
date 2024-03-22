# https://www.acmicpc.net/problem/17940
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    costs = [(INF, INF)] * n
    costs[0] = (0, 0)

    hq = []
    heappush(hq, (0, 0, 0))

    while hq:
        trans, money, now = heappop(hq)
        if now == m:
            return trans, money

        min_trans, min_money = costs[now]
        if min_trans < trans or (min_trans == trans and min_money < money):
            continue

        for nxt, nm in graph[now]:
            nxt_trans = trans + (1 if company[now] != company[nxt] else 0)
            nxt_money = money + nm

            save_trans, save_money = costs[nxt]
            if save_trans > nxt_trans or (save_trans == nxt_trans and save_money > nxt_money):
                costs[nxt] = (nxt_trans, nxt_money)
                heappush(hq, (nxt_trans, nxt_money, nxt))


n, m = map(int, input().split())
company = [int(input()) for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n):
    for j, w in enumerate(map(int, input().split())):
        if w:
            graph[i].append((j, w))

print(*dijkstra())