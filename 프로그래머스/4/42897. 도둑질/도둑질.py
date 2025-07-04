def solution(money):
    return max(get_max(money[1:]), get_max(money[2:-1]) + money[0])
    
    
def get_max(money):
    n = len(money)
    if n == 0:
        return 0
    elif n == 1:
        return money[0]
    
    dp = [0] * n
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
        
    return dp[n-1]