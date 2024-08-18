# https://www.acmicpc.net/problem/9344
import sys
input = sys.stdin.readline


def get_min_distance(pq):
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

    parent, rank, total = list(range(n+1)), [1] * (n+1), 0
    if pq:
        for u, v, w in costs:
            if (u, v) == (p, q) or (u, v) == (q, p):
                union(p, q)
                total = w
                break

    for u, v, w in costs:
        if find(u) != find(v):
            union(u, v)
            total += w

    return total


ans = []
for _ in range(int(input())):
    n, m, p, q = map(int, input().split())
    costs = [list(map(int, input().split())) for _ in range(m)]
    costs.sort(key=lambda cost: cost[2])

    ans.append('YES' if get_min_distance(0) == get_min_distance(1) else 'NO')

print('\n'.join(ans))