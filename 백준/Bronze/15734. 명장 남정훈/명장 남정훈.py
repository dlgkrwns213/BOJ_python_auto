l, r, a = map(int, input().split())

if l < r:
    use = min(a, r-l)
    l += use
    a -= use
else:
    use = min(a, l-r)
    r += use
    a -= use

print(2 * (min(l, r) + a // 2))