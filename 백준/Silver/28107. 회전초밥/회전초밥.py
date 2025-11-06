from collections import defaultdict, deque

n, m = map(int, input().split())
first = defaultdict(deque)
for idx in range(n):
    k, *eats = map(int, input().split())
    for eat in eats:
        first[eat].append(idx)

counts = [0] * n
for sushi in map(int, input().split()):
    if first[sushi]:
        counts[first[sushi].popleft()] += 1

print(' '.join(map(str, counts)))