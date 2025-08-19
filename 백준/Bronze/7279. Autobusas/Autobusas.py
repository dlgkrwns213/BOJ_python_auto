n, k = map(int, input().split())
now, ans = 0, 0

for _ in range(n):
    a, b = map(int, input().split())
    now += a - b

    ans = max(ans, now - k)

print(ans)