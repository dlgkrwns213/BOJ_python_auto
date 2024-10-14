# https://www.acmicpc.net/problem/19951
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
init = list(map(int, input().split()))

change = [0] * (n+1)
for _ in range(m):
    a, b, k = map(int, input().split())
    change[a-1] += k
    change[b] -= k

for i in range(n):
    change[i+1] += change[i]

print(' '.join(map(lambda idx: str(init[idx] + change[idx]), range(n))))