x, n = map(int, input().split())

for _ in range(n):
    x = (x << 1 if x % 2 else x >> 1) ^ 6

print(x)