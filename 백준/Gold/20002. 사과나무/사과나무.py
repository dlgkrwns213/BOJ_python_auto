# https://www.acmicpc.net/problem/20002
import sys
input = sys.stdin.readline

n = int(input())
trees = [list(map(int, input().split())) for _ in range(n)]

prefix = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + trees[i][j]

mx = -float('inf')
for size in range(1, n+1):
    for i in range(n-size+1):
        for j in range(n-size+1):
            now = prefix[i+size][j+size] - prefix[i+size][j] - prefix[i][j+size] + prefix[i][j]
            mx = max(mx, now)

print(mx)