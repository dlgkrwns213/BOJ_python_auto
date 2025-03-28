n, k = map(int, input().split())
flavors = list(map(int, input().split()))
flavors += flavors

now = sum(flavors[:k])
mx = now
for i in range(n):
    now += flavors[i+k] - flavors[i]
    mx = max(mx, now)
print(mx)