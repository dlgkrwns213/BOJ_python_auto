dp = [0] * 46
dp[0], dp[1] = 1, 1
for i in range(2, 46):
    dp[i] = dp[i-1] + dp[i-2]

print('\n'.join(map(lambda num: str(dp[num]), (int(input()) for _ in range(int(input()))))))