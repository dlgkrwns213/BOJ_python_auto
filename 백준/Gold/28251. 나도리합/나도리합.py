# https://www.acmicpc.net/problem/28251
import sys
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = map(find, (x, y))
    if x == y:
        return values[x][1]

    sum_x, mul_x = values[x]
    sum_y, mul_y = values[y]
    value = sum_x+sum_y, mul_x+mul_y+sum_x*sum_y
    if rank[x] >= rank[y]:
        rank[x] += rank[y]
        parent[y] = x
        values[x] = value
        return values[x][1]
    else:
        rank[y] += rank[x]
        parent[x] = y
        values[y] = value
        return values[y][1]


n, q = map(int, input().split())
sizes = [0] + list(map(int, input().split()))

parent, rank = list(range(n+1)), [1] * (n+1)
values = [(size, 0) for size in sizes]
ans = []
for _ in range(q):
    a, b = map(int, input().split())
    ans.append(union(a, b))
print('\n'.join(map(str, ans)))