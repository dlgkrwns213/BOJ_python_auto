# https://www.acmicpc.net/problem/2878
import sys
input = sys.stdin.readline
MOD = (1 << 64) - 1

m, n = map(int, input().split())
candies = sorted(int(input()) for _ in range(n))

left, right = 0, max(candies)
while left < right:
    mid = left + right >> 1
    c = sum(map(lambda candy: max(0, candy-mid), candies))

    if c <= m:
        right = mid
    else:
        left = mid + 1

rest = m-sum(map(lambda candy: max(0, candy-left), candies))
ans = sum(map(lambda candy: min(candy, left) ** 2, candies)) - (left**2 - (left-1)**2) * rest
print(ans & MOD)