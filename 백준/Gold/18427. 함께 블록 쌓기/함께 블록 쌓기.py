# https://www.acmicpc.net/problem/18427
import sys
input = sys.stdin.readline
MOD = 10007


def dfs(idx, rest):
    if idx == n:
        return 0 if rest else 1

    if dp[idx][rest] != -1:
        return dp[idx][rest]

    ret = 0
    for height in heights[idx]:
        if height > rest:
            break
        ret += dfs(idx+1, rest-height)
    ret %= MOD

    dp[idx][rest] = ret
    return ret


n, m, h = map(int, input().split())
heights = [[0] + sorted(map(int, input().split())) for _ in range(n)]

dp = [[-1]*(h+1) for _ in range(n)]
print(dfs(0, h))