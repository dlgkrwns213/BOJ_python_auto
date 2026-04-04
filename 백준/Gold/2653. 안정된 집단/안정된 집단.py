import sys
from collections import defaultdict
input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    fx, fy = map(find, (x, y))

    if fx > fy:
        parent[fy] = fx
    else:
        parent[fx] = fy


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
parent = list(range(n))
graph = [[] for _ in range(n+1)]
for i in range(n):
    for j in range(i):
        if not board[i][j]:
            union(i, j)

group_idxs = [0] * n
groups = defaultdict(list)
for i in range(n):
    group_idx = find(i)
    group_idxs[i] = group_idx
    groups[group_idx].append(i+1)

if any(len(group) == 1 for group in groups.values()):
    print(0)
    exit(0)

for i in range(n):
    for j in range(i):
        if (find(i) == find(j) and board[i][j]) or (find(i) != find(j) and not board[i][j]):
            print(0)
            exit(0)

print(len(groups))
for group in groups.values():
    print(' '.join(map(str, group)))