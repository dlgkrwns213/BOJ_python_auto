n = int(input())
dp = [0]*(n+1)
for i in range(2, n+1):
    if i%6==0:
        dp[i] = min(dp[i//3], dp[i//2], dp[i-1])+1
    elif i%3==0:
        dp[i] = min(dp[i//3], dp[i-1])+1
    elif i%2==0:
        dp[i] = min(dp[i//2], dp[i-1])+1
    else:
        dp[i] = dp[i-1]+1

print(dp[n])
while n>=1:
    print(n, end=' ')
    if n%6==0:
        m = min(dp[n-1], dp[n//3], dp[n//2])
        if m==dp[n-1]:
            n-=1
        elif m==dp[n//2]:
            n//=2
        elif m==dp[n//3]:
            n//=3
    elif n%3==0:
        m = min(dp[n-1], dp[n//3])
        if m==dp[n-1]:
            n-=1
        elif m==dp[n//3]:
            n//=3
    elif n%2==0:
        m = min(dp[n-1], dp[n//2])
        if m==dp[n-1]:
            n-=1
        elif m==dp[n//2]:
            n//=2
    else:
        n-=1