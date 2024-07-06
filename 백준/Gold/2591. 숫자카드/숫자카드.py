# https://www.acmicpc.net/problem/2591
s = input()

length = len(s)
if length == 1:
    print(1)
    exit(0)

dp = [0] * length
dp[0] = 1 if s[1] != '0' else 0
dp[1] = dp[0] + (1 if s[0:2] <= '34' else 0)

for i in range(2, length):
    if i < length-1 and s[i+1] == '0':
        continue
    dp[i] = dp[i-1] + (dp[i-2] if s[i-1:i+1] <= '34' else 0)

print(dp[-1])