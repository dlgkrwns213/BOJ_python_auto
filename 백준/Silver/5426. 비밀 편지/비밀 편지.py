import sys
from math import sqrt
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()

    n = int(sqrt(len(s)))
    board = [[s[i*n+j] for j in range(n)] for i in range(n)]

    ans = []
    for j in range(n-1, -1, -1):
        for i in range(n):
            ans.append(board[i][j])

    print(''.join(ans))