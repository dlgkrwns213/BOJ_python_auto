from math import floor, sqrt, log, sin
MAX = int(1e6)

dp = [0] * (MAX+1)
dp[0] = 1
for i in range(1, MAX+1):
    dp[i] = (dp[floor(i - sqrt(i))] + dp[floor(log(i))] + dp[floor(i * (sin(i) ** 2))]) % MAX

ans = []
while True:
    n = int(input())
    if n == -1:
        break
    ans.append(dp[n])
print('\n'.join(map(str, ans)))