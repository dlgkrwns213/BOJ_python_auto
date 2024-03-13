# https://www.acmicpc.net/problem/17612
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, k = map(int, input().split())
hq, not_used_counter, out_order, time = [], [], [0], 0
for _ in range(n):
    i, w = map(int, input().split())
    if len(hq) == k:
        time = hq[0][0]
        while hq and hq[0][0] == time:
            _, counter_idx, outer = heappop(hq)
            out_order.append(outer)
            heappush(not_used_counter, -counter_idx)

    if not_used_counter:
        counter_idx = heappop(not_used_counter)
    else:
        counter_idx = len(hq)
    heappush(hq, (time+w, -counter_idx, i))

while hq:
    _, _, outer = heappop(hq)
    out_order.append(outer)

print(sum(i*v for i, v in enumerate(out_order)))