import sys
from itertools import accumulate
input = sys.stdin.readline

n = int(input())
difficulties = list(map(int, input().split()))

mistakes = [0, 0] + [1 if difficulties[i] > difficulties[i+1] else 0 for i in range(n-1)] + [0]
prefix = list(accumulate(mistakes))

ans = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    ans.append(prefix[y]-prefix[x])
print('\n'.join(map(str, ans)))