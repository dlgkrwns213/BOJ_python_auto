# https://www.acmicpc.net/problem/18267
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
cows = ' ' + input().rstrip()

rank, parent = [1] * (n+1), list(range(n+1))
for _ in range(n-1):
    x, y = map(int, input().split())
    if cows[x] == cows[y]:
        union(x, y)

ans = []
for _ in range(m):
    *tmp, c = input().split()
    a, b = map(int, tmp)
    
    ans.append(1 if find(a) != find(b) or cows[find(a)] == c else 0)

print(''.join(map(str, ans)))