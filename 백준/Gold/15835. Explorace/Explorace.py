# https://www.acmicpc.net/problem/30797
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


ans = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    teams = [list(map(int, input().split())) for _ in range(m)]
    teams.sort(key=lambda team: team[2])

    parent, rank = list(range(n+1)), [1] * (n+1)
    total = 0
    for a, b, cost in teams:
        if find(a) != find(b):
            union(a, b)
            total += cost

    ans.append(total)

print('\n'.join(map(lambda idx: f'Case #{idx+1}: {ans[idx]} meters', range(len(ans)))))