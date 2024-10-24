import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')

n, m, k = map(int, input().split())
waits = [list(map(int, input().split())) for _ in range(n)]

# 줄 세우기
lines = [[(*waits[i * m + j], i*m+j) if i * m + j < len(waits) else (-INF, -INF, -1)
          for i in range((n + 2 * m - 1) // m)]
         for j in range(m)]

# 초기 heap 설정
line_idxs = [1] * m
hq = []
for line_idx in range(m):
    d, h, person_idx = lines[line_idx][0]
    heappush(hq, (-d, -h, line_idx, person_idx))

# person_idx가 k를 찾기
cnt = 0
while True:
    d, h, li, pi = heappop(hq)
    if pi == k:
        break
    cnt += 1

    nd, nh, npi = lines[li][line_idxs[li]]
    line_idxs[li] += 1
    heappush(hq, (-nd, -nh, li, npi))

print(cnt)