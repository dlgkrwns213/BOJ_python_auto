# https://www.acmicpc.net/problem/22254
from heapq import heappop, heappush, heapify


def possible(now: int) -> bool:
    hq = times[:now]
    heapify(hq)

    for time in times[now:]:
        nxt_time = heappop(hq) + time
        if nxt_time > x:
            return False

        heappush(hq, nxt_time)

    return True


n, x = map(int, input().split())
times = list(map(int, input().split()))

left, right = 1, n
while left < right:
    mid = left + right >> 1
    if possible(mid):
        right = mid
    else:
        left = mid+1

print(left)