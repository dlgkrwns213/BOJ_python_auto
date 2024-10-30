# https://www.acmicpc.net/problem/12004
import sys
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = map(find, (x, y))

    if rank[x] >= rank[y]:
        rank[x] += rank[y]
        parent[y] = x
    else:
        rank[y] += rank[x]
        parent[x] = y


n, m = map(int, input().split())
connects = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    connects[i][j] = 1
    connects[j][i] = 1

opened, ans = [], []
rank, parent = [1] * (n+1), list(range(n+1))
for now in [int(input()) for _ in range(n)][::-1]:
    for opn in opened:
        if connects[opn][now]:
            union(opn, now)
    opened.append(now)

    fo = find(opened[0])
    ans.append(1 if all(find(opn) == fo for opn in opened) else 0)

print('\n'.join(map(lambda x: 'YES' if x else 'NO', ans[::-1])))
