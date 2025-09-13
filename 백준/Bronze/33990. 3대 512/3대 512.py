INF = float("inf")

mn = INF
for _ in range(int(input())):
    now = sum(map(int, input().split()))
    if now >= 512:
        mn = min(mn, now)

print(mn if mn != INF else -1)