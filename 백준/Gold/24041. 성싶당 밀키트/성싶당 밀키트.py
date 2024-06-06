# https://www.acmicpc.net/problem/24041
import sys
input = sys.stdin.readline


def get_bacterias(day):
    bacteria = sum(map(lambda ingredient: ingredient[0] * max(1, day-ingredient[1]), imp))
    if uim_count > k:
        uim_bacteria = sum(sorted(map(lambda ingredient: ingredient[0] * max(1, day-ingredient[1]), uim))[:uim_count-k])
        bacteria += uim_bacteria
    return bacteria


n, g, k = map(int, input().split())
uim, imp = [], []
for _ in range(n):
    s, l, o = map(int, input().split())
    if o:
        uim.append((s, l))
    else:
        imp.append((s, l))

uim_count = len(uim)
left, right = 1, 2 * int(1e9) + 1
while left < right:
    mid = left + right >> 1
    if get_bacterias(mid) > g:
        right = mid
    else:
        left = mid + 1

print(left-1)