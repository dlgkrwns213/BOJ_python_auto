# https://www.acmicpc.net/problem/21773
import sys
from heapq import heappop, heappush
from collections import defaultdict
input = sys.stdin.readline

t, n = map(int, input().split())
hq, rest = [], [0] * 1000001
for _ in range(n):
    ids, id_rest, prior = map(int, input().split())
    heappush(hq, (-prior, ids))
    rest[ids] = id_rest

use = [-1] * t
time = 0
while time < t and hq:
    prior, ids = heappop(hq)
    use[time] = ids
    rest[ids] -= 1

    if rest[ids]:
        heappush(hq, (prior+1, ids))

    time += 1

print('\n'.join(map(str, use[:time])))