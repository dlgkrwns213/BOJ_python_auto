import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    n = int(input())

    x = int(n**0.5)
    left, right = x+1, x << 2
    while left < right:
        mid = left + right >> 1
        if mid * (mid+1) >> 1 > n:
            right = mid
        else:
            left = mid + 1
    ans.append(left-1)
print('\n'.join(map(str, ans)))