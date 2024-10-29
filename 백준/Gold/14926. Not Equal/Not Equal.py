# https://www.acmicpc.net/problem/14926
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def recursion(now):
    global order

    order.append(now)
    for nxt in range(n):
        if possible[now][nxt]:
            possible[now][nxt] = 0
            possible[nxt][now] = 0
            recursion(nxt)


n = int(input())

possible = [[1]*n for _ in range(n)]
for i in range(n):
    possible[i][i] = 0
possible[0][n-1] = 0
possible[n-1][0] = 0

order = []
recursion(0)
order.append(0)

print(' '.join(map(lambda num: f'a{num+1}', order)))