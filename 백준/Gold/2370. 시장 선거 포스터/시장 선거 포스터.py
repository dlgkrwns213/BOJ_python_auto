import sys
input = sys.stdin.readline

n = int(input())
posters = [list(map(int, input().split())) for _ in range(n)]

locations = set()
for poster in posters:
    locations |= set(poster)
indexes = {v: i for i, v in enumerate(sorted(locations))}

m = len(indexes)
colors = [0] * m
for i, (s, e) in enumerate(posters):
    for x in range(indexes[s], indexes[e]+1):
        colors[x] = i+1

print(len(set(colors)))