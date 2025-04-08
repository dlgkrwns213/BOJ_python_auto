import sys
from collections import Counter
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    n, x = map(int, input().split())
    counts = Counter(map(int, input().split()))

    if x:
        ans.append(sum(map(lambda key: counts[key] * counts[key ^ x], counts)) >> 1)
    else:
        ans.append(sum(map(lambda key: counts[key] * (counts[key]-1) >> 1, counts)))

print('\n'.join(map(str, ans)))