a, b = map(int, input().split())
k, x = map(int, input().split())

left = max(a, k-x)
right = min(b, k+x)

print(right - left + 1 if left <= right else 'IMPOSSIBLE')