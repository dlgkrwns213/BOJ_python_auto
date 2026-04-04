import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


n = int(input())
posters = [tuple(map(int, input().split())) for _ in range(n)]

coords = set()
for poster in posters:
    coords |= set(poster)

coords = sorted(coords)
comp = {x: i for i, x in enumerate(coords)}

parent = list(range(len(coords)+1))
visible = 0

for i in range(n-1, -1, -1):
    l, r = posters[i]
    l = comp[l]
    r = comp[r]

    x = find(l)
    seen = False

    while x <= r:
        seen = True
        parent[x] = x+1
        x = find(x)

    if seen:
        visible += 1

print(visible)