a, b, n, w = map(int, input().split())

x, y = max(a, b), min(a, b)
if x == y:
    if n == 2 and a+b == w:
        print(1, 1)
    else:
        print(-1)
elif n * y < w < n * x:
    gap = n * x - w
    if gap % (x-y):
        print(-1)
    else:
        t = gap // (x-y)
        if a < b:
            print(t, n-t)
        else:
            print(n-t, t)
else:
    print(-1)