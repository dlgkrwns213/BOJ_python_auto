# https://www.acmicpc.net/problem/23843
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
times = list(map(int, input().split()))

if n <= m:
    print(max(times))
else:
    times.sort(reverse=True)
    hq = []
    for i in range(m):
        heappush(hq, times[i])

    for i in range(m, n):
        x = heappop(hq)
        heappush(hq, x + times[i])

    print(max(hq))