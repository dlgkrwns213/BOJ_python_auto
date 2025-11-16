n, x = map(int, input().split())
a = list(map(int, input().split()))

mn = float('inf')
for i in range(1, n):
    mn = min(mn, a[i] + a[i-1])

print(mn * x)