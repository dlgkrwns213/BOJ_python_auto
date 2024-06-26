# https://www.acmicpc.net/problem/1994
import sys
from bisect import bisect_left
sys.setrecursionlimit(10**4)
input = sys.stdin.readline


def find(x, y):
    if dp[x][y] != 1:
        return dp[x][y]

    ret = 2
    find_num = 2 * nums[y] - nums[x]
    z = bisect_left(nums, find_num, y+1)
    if z < len(nums) and nums[z] == find_num:
        ret = find(y, z) + 1

    dp[x][y] = ret
    return ret


n = int(input())
nums = sorted(int(input()) for _ in range(n))

dp = [[1]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        find(i, j)

print(max(map(max, dp)))