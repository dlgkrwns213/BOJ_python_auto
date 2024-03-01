import sys
input = sys.stdin.readline


n, k = map(int, input().split())
drinks = [int(input()) for _ in range(n)]

left, right = 0, max(drinks) + 1
while left < right:
    mid = left + right >> 1
    now = sum(map(lambda drink: drink // mid, drinks))
    if now < k:
        right = mid
    else:
        left = mid + 1

print(left-1)