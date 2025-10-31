import sys
from bisect import bisect_right
input = sys.stdin.readline

n, q = map(int, input().split())
b = [int(input()) for _ in range(n)]

prefix = [0] * n
prefix[0] = b[0]
for i in range(1, n):
    prefix[i] = prefix[i-1] + b[i]

ans = []
for _ in range(q):
    t = int(input())
    ans.append(bisect_right(prefix, t)+1)
print('\n'.join(map(str, ans)))