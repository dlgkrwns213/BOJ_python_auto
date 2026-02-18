INF = float('inf')

n = int(input())
scores = list(map(int, input().split()))

dp = [[-INF]*4 for _ in range(n)]

dp[0][0] = scores[0]
dp[0][1] = 2 * scores[0]
for i, score in enumerate(scores[1:], 1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][3]) + score
    dp[i][1] = max(dp[i-1][0], dp[i-1][3]) + 2*score
    dp[i][2] = dp[i-1][1] + 2*score
    dp[i][3] = dp[i-1][2] + 2*score

print(max(dp[-1]))