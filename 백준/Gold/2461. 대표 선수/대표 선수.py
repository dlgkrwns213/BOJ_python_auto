# https://www.acmicpc.net/problem/2461
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e10)

n, m = map(int, input().split())

classes = []
hq, mx, use = [], 0, [0] * n
for idx in range(n):
    c = sorted(map(int, input().split()))
    classes.append(c)

    mx = max(mx, c[0])
    heappush(hq, (c[0], idx))

ans = INF
while hq:
    mn, idx = heappop(hq)

    ans = min(ans, mx-mn)
    if use[idx] == m:
        break

    idx_class_nxt = classes[idx][use[idx]]
    heappush(hq, (idx_class_nxt, idx))
    mx = max(mx, idx_class_nxt)

    use[idx] += 1

print(ans)