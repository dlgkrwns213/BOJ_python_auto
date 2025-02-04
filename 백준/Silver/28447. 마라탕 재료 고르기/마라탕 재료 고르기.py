import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
compatibilities = [list(map(int, input().split())) for _ in range(n)]

mx = -float('inf')
for materials in combinations(range(n), k):
    mx = max(mx, sum(compatibilities[material_i][material_j]
                     for i, material_i in enumerate(materials)
                     for material_j in materials[:i]))
print(mx)