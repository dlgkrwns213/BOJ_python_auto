# https://www.acmicpc.net/problem/10021
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


def get_distance(loc1, loc2):
    x1, y1 = loc1
    x2, y2 = loc2
    return (x1-x2) ** 2 + (y1-y2) ** 2


n, c = map(int, input().split())
locations = [list(map(int, input().split())) for _ in range(n)]

pipes = [i*n+j+get_distance(locations[i], locations[j])*n*n
         for i in range(n) for j in range(i)
         if get_distance(locations[i], locations[j]) >= c]
pipes.sort()

parent, rank, total = list(range(n)), [1] * n, 0
for pipe in pipes:
    pipe, j = divmod(pipe, n)
    length, i = divmod(pipe, n)
    if find(i) != find(j):
        union(i, j)
        total += length

zero = find(0)
print(total if all(find(node) == zero for node in range(1, n)) else -1)