# https://www.acmicpc.net/problem/17179
import sys
input = sys.stdin.readline


def cutting(length):
    now, cnt = 0, 0
    for location in locations:
        if location - now > length:
            now = location
            cnt += 1

    return True if cnt > q else False


n, m, l = map(int, input().split())
locations = [int(input()) for _ in range(m)] + [l]
mn = min(map(lambda i: locations[i+1]-locations[i], range(m)))

ans = []
for _ in range(n):
    q = int(input())

    left, right = mn, l
    while left < right:
        mid = left + right >> 1
        if cutting(mid):
            left = mid + 1
        else:
            right = mid

    ans.append(left)

print('\n'.join(map(str, ans)))
