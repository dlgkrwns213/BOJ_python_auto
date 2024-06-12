# https://www.acmicpc.net/problem/15586
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
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]


n, q = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(n-1)]
relations.sort(key=lambda relation:  -relation[2])

queries = [list(map(int, input().split())) + [idx] for idx in range(q)]
queries.sort(reverse=True)

ans, ri = [-1] * q, 0
parent, rank = list(range(n+1)), [1] * (n+1)
for k, v, idx in queries:
    while ri < n-1:
        p, q, r = relations[ri]
        if r < k:
            break
        union(p, q)
        ri += 1

    ans[idx] = rank[find(v)] - 1

print('\n'.join(map(str, ans)))