# https://www.acmicpc.net/problem/12763
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    xt = mx_time + 1

    moneys = [INF] * (n+1) * xt
    moneys[xt] = 0

    hq = []
    heappush(hq, (0, xt))

    while hq:
        money, tn = heappop(hq)
        now, time = divmod(tn, xt)
        if now == n:
            return money
        if moneys[now * xt + time] < money:
            continue

        for nxt, nt, nm in graph[now]:
            nxt_time = nt + time
            nxt_money = nm + money
            if nxt_time > mx_time or nxt_money > mx_money:
                continue
            nxt_tn = nxt * xt + nxt_time
            if moneys[nxt_tn] > nxt_money:
                moneys[nxt_tn] = nxt_money
                heappush(hq, (nxt_money, nxt_tn))
    return -1


n = int(input())
mx_time, mx_money = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b, t, m = map(int, input().split())
    graph[a].append((b, t, m))
    graph[b].append((a, t, m))

print(dijkstra())