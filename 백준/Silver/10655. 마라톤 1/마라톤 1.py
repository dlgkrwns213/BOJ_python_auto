import sys
input = sys.stdin.readline


def get_distances(p1: tuple, p2: tuple):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


n = int(input())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]

distances = list(map(lambda i: get_distances(checkpoints[i+1], checkpoints[i]), range(n-1)))
mn = float('inf')
for i in range(1, n-1):
    now = get_distances(checkpoints[i+1], checkpoints[i-1]) - distances[i-1] - distances[i]
    mn = min(mn, now)

print(mn + sum(distances))