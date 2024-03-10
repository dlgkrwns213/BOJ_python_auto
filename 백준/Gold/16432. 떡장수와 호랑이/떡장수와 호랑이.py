# https://www.acmicpc.net/problem/16432
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(idx, now):
    if idx == n:
        return
    if dp[idx][now]:
        return

    for nxt in days[idx]:
        if now == nxt:
            continue

        dfs(idx+1, nxt)
        dp[idx+1][nxt] = now


n = int(input())
days = [list(map(int, input().split()[1:])) for _ in range(n)]

dp = [[0]*10 for _ in range(n+1)]
dfs(0, -1)

r = -1
for i in range(10):
    if dp[-1][i]:
        r = i
        break

if r == -1:
    print(-1)
else:
    ans = [r]
    for i in range(n, 1, -1):
        r = dp[i][r]
        ans.append(r)

    print('\n'.join(map(str, ans[::-1])))