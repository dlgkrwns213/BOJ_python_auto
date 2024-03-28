# https://www.acmicpc.net/problem/2283
n, k = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(n)]

mx = max(map(lambda line: line[1], lines)) + 1

# prefix sum
prefix = [0] * mx
for start, end in lines:
    prefix[start] += 1
    prefix[end] -= 1

for i in range(1, mx):
    prefix[i] += prefix[i-1]

# two points
left, right, now = 0, 0, 0
possible = False
while right < mx:
    if now < k:
        now += prefix[right]
        right += 1
    elif now > k:
        now -= prefix[left]
        left += 1
    else:  # now == find
        possible = True
        break

ans = (left, right) if possible else (0, 0)
print(*ans)