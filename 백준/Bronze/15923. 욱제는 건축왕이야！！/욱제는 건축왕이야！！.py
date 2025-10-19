n = int(input())
locs = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    x, y = locs[i]
    nx, ny = locs[i-1]

    ans += abs(nx - x) + abs(ny - y)

print(ans)