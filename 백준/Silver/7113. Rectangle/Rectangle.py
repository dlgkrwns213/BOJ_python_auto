n, m = map(int, input().split())
if n < m:
    n, m = m, n

cnt = 0
while m:
    c, r = divmod(n, m)
    cnt += c
    n, m = m, r

print(cnt)