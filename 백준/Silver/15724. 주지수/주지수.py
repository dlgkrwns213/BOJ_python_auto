import sys
input = sys.stdin.readline

n, m = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(n)]

prefix = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + people[i][j]

k = int(input())
ans = [0] * k
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    ans[i] = prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]

print('\n'.join(map(str, ans)))