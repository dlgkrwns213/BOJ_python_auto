a, b, c, d = map(int, input().split())

x = a * b
y = c * d

print("EMP"[(x > y) - (y > x)])