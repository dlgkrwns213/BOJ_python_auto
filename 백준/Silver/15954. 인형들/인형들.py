from math import sqrt

n, k = map(int, input().split())
prefers = list(map(int, input().split()))

mn = float('inf')
for i in range(n):
    for j in range(i+k-1, n):
        cnt = j - i + 1
        total = sum(prefers[i:j+1])

        x = sum(map(lambda idx: (prefers[idx] * cnt - total) ** 2, range(i, j+1)))
        mn = min(mn, x / (cnt * cnt * cnt))

print(sqrt(mn))