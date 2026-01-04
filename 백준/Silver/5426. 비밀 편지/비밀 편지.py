import sys
from math import sqrt
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    s = input().rstrip()

    n = int(sqrt(len(s)))
    for j in range(n-1, -1, -1):
        for i in range(n):
            ans.append(s[i*n+j])
    ans.append('\n')

print(''.join(ans))