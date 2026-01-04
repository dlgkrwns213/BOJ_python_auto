import sys
from math import sqrt
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()

    ans = []
    n = int(sqrt(len(s)))
    for j in range(n-1, -1, -1):
        for i in range(n):
            ans.append(s[i*n+j])
    print(''.join(ans))