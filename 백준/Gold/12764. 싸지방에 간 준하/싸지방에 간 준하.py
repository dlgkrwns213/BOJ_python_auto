# https://www.acmicpc.net/problem/12764
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
times = sorted(list(map(int, input().split())) for _ in range(n))

hq, not_used, count = [], [], [0] * (n+1)
for p, q in times:
    if hq and hq[0][0] <= p:
        while True:
            if not hq or hq[0][0] > p:
                break

            _, idx = heappop(hq)
            heappush(not_used, idx)

    if not not_used:
        count[len(hq)] += 1
        heappush(hq, (q, len(hq)))
    else:
        idx = heappop(not_used)
        count[idx] += 1
        heappush(hq, (q, idx))

x = next((i for i, v in enumerate(count) if not v), 0)
print(x)
print(' '.join(map(str, count[:x])))