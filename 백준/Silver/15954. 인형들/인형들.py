from math import sqrt

n, k = map(int, input().split())
prefers = list(map(int, input().split()))

mn = float('inf')
for count in range(k, n+1):
    total = sum(prefers[:count])
    square_total = sum(map(lambda x: x**2, prefers[:count]))

    start = 0
    while 1:
        var = count * square_total - 2 * (total ** 2) + (total ** 2)
        mn = min(mn, var/(count ** 2))

        nxt = start + count
        if nxt >= n:
            break

        total += prefers[nxt] - prefers[start]
        square_total += prefers[nxt] ** 2 - prefers[start] ** 2
        start += 1

print(sqrt(mn))