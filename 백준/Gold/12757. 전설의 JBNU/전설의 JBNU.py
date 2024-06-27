# https://www.acmicpc.net/problem/12757
import sys
from bisect import bisect_left, insort
input = sys.stdin.readline
INF = float('inf')


def add(key):
    ...


def find_idx(key):
    idx = bisect_left(keys, key)
    small, big = keys[idx-1], keys[idx]
    small_gap, big_gap = key - small, big - key
    if min(small_gap, big_gap) > k:
        return -1
    if small_gap < big_gap:
        return idx - 1
    elif small_gap > big_gap:
        return idx
    else:
        return -2


n, m, k = map(int, input().split())
keys, values = [0] * (n+2), dict()
for i in range(1, n+1):
    key, value = map(int, input().split())
    keys[i] = key
    values[key] = value
keys[0], keys[-1] = -INF, INF
keys.sort()

ans = []
for _ in range(m):
    command, *tmp = map(int, input().split())
    if command == 1:
        key, value = tmp
        insort(keys, key)
        values[key] = value
    elif command == 2:
        key, value = tmp
        idx = find_idx(key)
        if idx >= 0:
            values[keys[idx]] = value
    else:
        [key] = tmp
        idx = find_idx(key)
        if idx >= 0:
            added = values[keys[idx]]
        elif idx == -1:
            added = -1
        else:
            added = '?'
        ans.append(added)

print('\n'.join(map(str, ans)))