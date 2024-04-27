# https://www.acmicpc.net/problem/6137
import sys
input = sys.stdin.readline

n = int(input())
s = ''.join(input().rstrip() for _ in range(n))

t = []
left, right = 0, n-1
while left <= right:
    if s[left] < s[right]:
        t.append(s[left])
        left += 1
    elif s[left] > s[right]:
        t.append(s[right])
        right -= 1
    else:
        l, r = left, right
        while l <= r and s[l] == s[r]:
            l += 1
            r -= 1

        if s[l] < s[r]:
            now = s[left]
            while left <= right and now == s[left]:
                t.append(now)
                left += 1
        else:
            now = s[right]
            while left <= right and now == s[right]:
                t.append(now)
                right -= 1

for i in range(0, n, 80):
    print(''.join(t[i:i+80]))