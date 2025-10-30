# https://www.acmicpc.net/problem/27896
from heapq import heappush, heappop

n, m = map(int, input().split())
hq, now, cnt = [], 0, 0
for x in map(int, input().split()):
    heappush(hq, -x)

    while now + x >= m:
        now += 2*heappop(hq)
        cnt += 1
    now += x

print(cnt)