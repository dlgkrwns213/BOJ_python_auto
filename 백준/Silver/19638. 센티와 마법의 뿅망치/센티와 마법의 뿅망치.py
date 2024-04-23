import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, h, t = map(int, input().split())
hq = []
for _ in range(n):
    heappush(hq, -int(input()))

ans = t
for time in range(t):
    mx = -heappop(hq)
    if mx < h:
        heappush(hq, -mx)
        ans = time
        break

    if mx != 1:
        mx >>= 1
    heappush(hq, -mx)

if -hq[0] < h:
    print(f'YES\n{ans}')
else:
    print(f'NO\n{-hq[0]}')