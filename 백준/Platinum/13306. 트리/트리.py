# https://www.acmicpc.net/problem/13306
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
        return

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y


n, q = map(int, input().split())
parents = [[], []] + [list(map(int, input().split())) for _ in range(n-1)]

commands, later = [None] * (n-1+q), [False] * (n+1)
for i in range(n-1+q):
    command = list(map(int, input().split()))
    commands[i] = command
    if not command[0]:
        later[command[1]] = True

parent, rank = list(range(n+1)), [1] * (n+1)
for c in range(2, n+1):
    if later[c]:
        continue
    for p in parents[c]:
        union(c, p)

ans = []
for command in commands[::-1]:
    if not command[0]:
        b = command[1]
        for bp in parents[b]:
            union(b, bp)
    else:
        c, d = command[1:]
        ans.append('YES' if find(c) == find(d) else 'NO')

print('\n'.join(ans[::-1]))