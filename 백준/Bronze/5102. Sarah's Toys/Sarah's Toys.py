while True:
    n, m = map(int, input().split())
    if not n and not m:
        break

    k = n - m 
    if k % 2 == 1 and k >= 3:
        t = 1
        p = (k - 3) // 2
    else:
        t = 0
        p = k // 2

    print(p, t)