import sys
from heapq import heappop, heappush
input = sys.stdin.readline

hq, ans = [], []
for _ in range(int(input())):
    _, *presents = map(int, input().split())
    if presents:
        for present in presents:
            heappush(hq, -present)
    else:
        ans.append(-heappop(hq) if hq else -1)

print('\n'.join(map(str, ans)))