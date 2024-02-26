n = int(input())
for t in range(1, int(1e9)):
    if n == 1:
        break

    if n % 2:
        n = 3 * n + 1
    else:
        n >>= 1

print(t)