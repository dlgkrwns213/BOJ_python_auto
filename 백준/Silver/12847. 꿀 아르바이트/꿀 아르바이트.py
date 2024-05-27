n, m = map(int, input().split())
moneys = list(map(int, input().split()))

now = sum(moneys[:m])
mx = now
for i, money in enumerate(moneys[m:]):
    now += money - moneys[i]
    mx = max(mx, now)
print(mx)