# https://www.acmicpc.net/problem/2616
n = int(input())
nums = list(map(int, input().split()))
k = int(input())

prefix = [0] * (n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + nums[i]

dp = [[0]*(n+1) for _ in range(3)]
for i in range(3):
    for j in range(1, n+1):
        if j >= k:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + prefix[j] - prefix[j-k])
        else:
            dp[i][j] = dp[i-1][j-1]

print(dp[-1][-1])