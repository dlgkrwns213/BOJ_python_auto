a, b = map(int, input().split())

mn = max((a+1) // 2, (b+1) // 2)
mx = min(a, b)

print(mn, mx)