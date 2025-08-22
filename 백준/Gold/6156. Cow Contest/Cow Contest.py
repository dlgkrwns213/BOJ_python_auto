# https://www.acmicpc.net/problem/6156
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

ans = 0
for i in range(1, n+1):
    wins = sum(graph[i])
    loses = sum(graph[j][i] for j in range(1, n+1))

    # 나에게 이기는 수와 진 수의 합이 n-1인 경우 내 순위는 정해진 것임
    if wins + loses == n - 1:
        ans += 1

print(ans)