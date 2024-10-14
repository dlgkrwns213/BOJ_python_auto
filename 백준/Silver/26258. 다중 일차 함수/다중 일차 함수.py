import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
xs, slopes = [0] * n, [0] * n
bx, by = map(int, input().split())
xs[0] = bx
for i in range(1, n):
    x, y = map(int, input().split())
    xs[i] = x
    slopes[i] = (y > by) - (y < by)
    bx, by = x, y

k = int(input())
ans = [0] * k
for i in range(k):
    ans[i] = slopes[bisect_left(xs, float(input()))]

print('\n'.join(map(str, ans)))