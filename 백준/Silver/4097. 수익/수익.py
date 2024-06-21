import sys
input = sys.stdin.readline

ans = []
while True:
    n = int(input())
    if not n:
        break

    profits = [int(input()) for _ in range(n)]
    mx, now = 0, 0
    for profit in profits:
        now += profit
        if now < 0:
            now = 0
        mx = max(mx, now)

    ans.append(mx if mx else max(profits))

print('\n'.join(map(str, ans)))