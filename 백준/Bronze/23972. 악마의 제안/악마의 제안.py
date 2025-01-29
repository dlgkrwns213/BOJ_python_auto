k, n = map(int, input().split())

print((k * n + n - 2) // (n - 1) if n != 1 else -1)