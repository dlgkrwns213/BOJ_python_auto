n, m = map(int, input().split())

for l in range(28, 32):
    if (m+13) % l + 1 == n:
        print((m+6) % l + 1)
        break