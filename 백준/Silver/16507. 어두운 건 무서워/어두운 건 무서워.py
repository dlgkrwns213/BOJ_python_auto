import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
pixels = [list(map(int, input().split())) for _ in range(r)]

prefix = [[0]*(c+1) for _ in range(r+1)]
for i in range(1, r+1):
    for j in range(1, c+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + pixels[i-1][j-1]

ans = []
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    cnt = (r2 - r1 + 1) * (c2 - c1 + 1)
    total = prefix[r2][c2] - prefix[r1-1][c2] - prefix[r2][c1-1] + prefix[r1-1][c1-1]
    ans.append(total//cnt)

print('\n'.join(map(str, ans)))