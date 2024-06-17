# https://www.acmicpc.net/problem/27945
import sys
input = sys.stdin.readline


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    x = find(a)
    y = find(b)
    if x == y:
        return True

    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]


n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
roads.sort(key=lambda road: road[2])

parent, rank = list(range(n+1)), [1] * (n+1)
day = 1
for u, v, d in roads:
    if day != d or union(u, v):
        break
    day += 1

print(day)