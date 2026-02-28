n = int(input())
r = list(map(int, input().split()))

if n == 1:
    print(0)
    exit(0)

dp = [[0]*2 for _ in range(n)]
dp[0][0] = 0
dp[0][1] = r[0]

dp[1][0] = r[0]
dp[1][1] = r[1]

for i in range(2, n):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = min(dp[i-1]) + r[i]

print(min(dp[-1]))