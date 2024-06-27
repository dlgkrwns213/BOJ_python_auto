# https://www.acmicpc.net/problem/2342
INF = float('inf')
cost = [[0, 2, 2, 2, 2],
        [2, 0, 3, 4, 3],
        [2, 3, 0, 3, 4],
        [2, 4, 3, 0, 3],
        [2, 3, 4, 3, 0]]

buttons = list(map(int, input().split()[:-1]))

n = len(buttons)
dp = [[INF]*25 for _ in range(n+1)]
dp[-1][0] = 0
for i, button in enumerate(buttons):
    for num in range(25):
        x, y = divmod(num, 5)
        if button in (x, y):
            dp[i][num] = min(dp[i][num], dp[i-1][num] + 1)
        else:
            change_x = cost[x][button]
            nxt_x = button * 5 + y
            dp[i][nxt_x] = min(dp[i][nxt_x], dp[i-1][num] + change_x)

            change_y = cost[y][button]
            nxt_y = x * 5 + button
            dp[i][nxt_y] = min(dp[i][nxt_y], dp[i-1][num] + change_y)

print(min(dp[-2]))