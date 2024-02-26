# https://www.acmicpc.net/problem/15732
import sys
input = sys.stdin.readline


def get_acorns(box):
    acorns = 0
    for a, b, c in rules:
        if box < a:
            continue
        acorns += (min(b, box) - a) // c + 1

    return acorns


n, k, d = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(k)]

left, right = 1, n
while left < right:
    mid = left + right >> 1

    now = get_acorns(mid)
    if now >= d:
        right = mid
    else:
        left = mid + 1

print(left)