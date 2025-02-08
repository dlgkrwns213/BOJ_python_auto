# https://www.acmicpc.net/problem/2694
import sys
from itertools import accumulate
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    m = int(input())
    nums = [num for _ in range((m + 9) // 10) for num in map(int, input().split())]

    total = sum(nums)
    prefix_sum = list(accumulate(nums))

    for ps in prefix_sum:
        if total % ps or total // ps > m:
            continue

        need = ps
        possible = True
        for num in prefix_sum:
            if num < need:
                continue
            elif num == need:
                need += ps
            else:
                possible = False

        if possible:
            ans.append(ps)
            break

print('\n'.join(map(str, ans)))