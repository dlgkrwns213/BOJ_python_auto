# https://www.acmicpc.net/problem/32198
import sys
input = sys.stdin.readline
INF = float('inf')


def calculate(x, y):
    for j in range(x, y):
        dp[i][j] = min(dp[i-1][j-1] + 1, dp[i-1][j], dp[i-1][j+1] + 1)


n = int(input())
mx = 0
times: list[tuple or None] = [None] * 1001
for _ in range(n):
    t, a, b = map(int, input().split())
    times[t] = (a+1000, b+1000)
    mx = max(t, mx)

dp = [[INF]*2002 for _ in range(mx+1)]
dp[0][1000] = 0

for i in range(1, mx+1):
    if times[i]:
        a, b = times[i]
        calculate(0, a+1)
        calculate(b, 2001)
    else:
        calculate(0, 2001)

ans = min(dp[-1])
print(ans if ans != INF else -1)