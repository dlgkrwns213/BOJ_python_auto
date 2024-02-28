import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, m = map(int, input().split())
points = sorted(map(int, input().split()))

ans = [0] * m
for tc in range(m):
    start, end = map(int, input().split())
    ans[tc] = bisect_right(points, end) - bisect_left(points, start)

print('\n'.join(map(str, ans)))