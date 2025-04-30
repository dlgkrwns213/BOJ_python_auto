def getCount(now):
    return now - now // 3 - now // 5 + now // 15


n = int(input())
left, right = n, 3*n
while left < right:
    mid = left + right >> 1
    if getCount(mid) >= n:
        right = mid
    else:
        left = mid + 1

print(left)