# https://www.acmicpc.net/problem/16566
from bisect import bisect_right


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(down, up):
    x = find(down)
    y = find(up)

    parent[x] = y


n, m, k = map(int, input().split())
cards = sorted(map(int, input().split()))

ans, parent = [], list(range(m+1))
for cs in map(int, input().split()):
    ms_idx = bisect_right(cards, cs)
    fms = find(ms_idx)
    ans.append(cards[fms])
    union(fms, fms+1)

print('\n'.join(map(str, ans)))