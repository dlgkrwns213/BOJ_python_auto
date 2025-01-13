k, w, m = map(int, input().split())
print(max((w - k + m - 1) // m, 0))