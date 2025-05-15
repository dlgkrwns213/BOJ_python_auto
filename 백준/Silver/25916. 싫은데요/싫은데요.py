n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 0
mx, v = 0, 0;
while right < n:
    v += a[right]
    right += 1

    while v > m:
        v -= a[left]
        left += 1

    mx = max(mx, v)

print(mx)