n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, min(a) * m
while left < right:
    mid = left + right >> 1
    if sum(map(lambda time: mid // time, a)) < m:
        left = mid + 1
    else:
        right = mid

print(left)