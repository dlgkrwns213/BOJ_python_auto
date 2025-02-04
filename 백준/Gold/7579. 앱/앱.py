# https://www.acmicpc.net/problem/7579
n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

total = sum(costs) 
dp = [0] * (total+1)

for i, memory in enumerate(memories):
    ci = costs[i]
    for cost in range(total, ci-1, -1):
        dp[cost] = max(dp[cost], dp[cost-ci] + memory)

for cost, memory in enumerate(dp):
    if memory >= m:
        print(cost)
        break