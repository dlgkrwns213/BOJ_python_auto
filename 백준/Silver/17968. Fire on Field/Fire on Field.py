n = int(input())
a = [0] * (n+1)
a[0] = 1
if n >= 1:
    a[1] = 1

for i in range(2, n+1):
    cand = 1
    while True:
        ok = True
        for k in range(1, (i >> 1) + 1):
            if i - 2 * k >= 0:
                if cand - a[i-k] == a[i-k] - a[i-2*k]:
                    ok = False
                    break
        if ok:
            a[i] = cand
            break
        cand += 1

print(a[n])