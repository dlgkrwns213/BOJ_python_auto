import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def possible(now):
    prefers = [prefer for prefer, level in beers if level <= now]
    return sum(prefers[:n]) if len(prefers) >= n else -1


n, m, k = map(int, input().split())
beers = [list(map(int, input().split())) for _ in range(k)]  # 선호도 도수레벨
beers.sort(key=lambda beer: -beer[0])

INF = (k << 31) + 1
left, right = 0, INF
while left < right:
    mid = left + right >> 1
    if possible(mid) >= m:
        right = mid
    else:
        left = mid + 1

print(left if left != INF else -1)