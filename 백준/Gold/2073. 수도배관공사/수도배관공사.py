# https://www.acmicpc.net/problem/2073
import sys
input = sys.stdin.readline

d, p = map(int, input().split())
pipes = [list(map(int, input().split())) for _ in range(p)]

dp = [0] * (d+1)
dp[0] = int(1e9)
for l, c in pipes:
    for w in range(d, l-1, -1):
        dp[w] = max(dp[w], min(dp[w-l], c))

print(dp[d])