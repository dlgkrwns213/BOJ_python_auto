n, k = map(int, input().split())
a: list = list(map(int, input().split()))

mn = 1000 * n
for i, v in enumerate(a):
    x = v - k * i
    if x > 0:
        now = len([j for j, w in enumerate(a) if w == k * j + x])
        mn = min(mn, n-now)
print(mn)