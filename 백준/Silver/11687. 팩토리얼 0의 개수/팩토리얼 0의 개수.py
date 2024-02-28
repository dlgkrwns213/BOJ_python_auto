def find_five(num):
    ret = 0
    while num:
        ret += num // 5
        num //= 5
    return ret


m = int(input())
left, right = 0, 5*m
while left < right:
    mid = left + right >> 1
    if find_five(mid) >= m:
        right = mid
    else:
        left = mid + 1

print(left if find_five(left) == m else -1)