h, y = map(int, input().split())

dp = [0] * (y+5)
dp[0] = h
for i in range(1, y+1):
    one = int(dp[i-1] * 1.05)
    three = int(dp[i-3] * 1.2)
    five = int(dp[i-5] * 1.35)

    dp[i] = max(one, three, five)

print(dp[y])