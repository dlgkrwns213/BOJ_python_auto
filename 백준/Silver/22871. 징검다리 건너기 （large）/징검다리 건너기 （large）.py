INF = float('inf')

n = int(input())
stones = list(map(int, input().split()))

dp = [INF] * n
dp[0] = 0
for i, stonei in enumerate(stones):
    for j, stonej in enumerate(stones[:i]):
        dp[i] = min(dp[i], max(dp[j], (i-j) * (1 + abs(stonei - stonej))))

print(dp[-1])