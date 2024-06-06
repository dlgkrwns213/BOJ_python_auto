# https://www.acmicpc.net/problem/18116
import sys
input = sys.stdin.readline
MAX = int(1e6)


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    x = find(a)
    y = find(b)
    if x == y:
        return

    if count[x] < count[y]:
        parent[x] = y
        count[y] += count[x]
    else:
        parent[y] = x
        count[x] += count[y]


ans = []
parent, count = list(range(MAX+1)), [1] * (MAX+1)
for _ in range(int(input())):
    q, *tmp = input().split()
    if q == 'I':
        a, b = map(int, tmp)
        union(a, b)
    else:
        c = int(*tmp)
        ans.append(count[find(c)])

print('\n'.join(map(str, ans)))