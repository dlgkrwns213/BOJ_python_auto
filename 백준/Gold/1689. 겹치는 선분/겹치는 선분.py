# https://www.acmicpc.net/problem/1689
import sys
input = sys.stdin.readline

n = int(input())
counts = dict()
for _ in range(n):
    start, end = map(int, input().split())
    counts[start] = counts.get(start, 0) + 1
    counts[end] = counts.get(end, 0) - 1

locs = sorted(counts.keys())
now, mx = 0, 0
for loc in locs:
    now += counts[loc]
    mx = max(mx, now)

print(mx)