import sys
input = sys.stdin.readline


def bisect_left(point):
    left, right = 0, n
    while left < right:
        mid = left + right >> 1
        if points[mid] >= point:
            right = mid
        else:
            left = mid + 1
    return left


def bisect_right(point):
    left, right = 0, n
    while left < right:
        mid = left + right >> 1
        if points[mid] > point:
            right = mid
        else:
            left = mid + 1
    return left


n, m = map(int, input().split())
points = sorted(map(int, input().split()))

ans = [0] * m
for tc in range(m):
    start, end = map(int, input().split())
    ans[tc] = bisect_right(end) - bisect_left(start)

print('\n'.join(map(str, ans)))