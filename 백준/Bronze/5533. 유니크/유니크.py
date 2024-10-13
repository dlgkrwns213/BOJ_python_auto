import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
scores = [0] * n
for row in zip(*(list(map(int, input().split())) for _ in range(n))):
    counts = Counter(row)
    for idx, card in enumerate(row):
        scores[idx] += card if counts[card] == 1 else 0

print('\n'.join(map(str, scores)))