# https://www.acmicpc.net/problem/17490
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
if m <= 1:
    print('YES')
    exit(0)

s = list(map(int, input().split())) * 2

boundaries = []
for _ in range(m):
    i, j = map(int, input().split())
    if i > j:
        i, j = j, i

    boundaries.append(j if i == 1 and j == n else i)
boundaries.sort()
boundaries.append(boundaries[0]+n)

total = sum(map(lambda idx: min(s[boundaries[idx]:boundaries[idx+1]]), range(m)))
print('YES' if total <= k else 'NO')