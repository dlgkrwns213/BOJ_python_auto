n, k = map(int, input().split())
a = list(map(int, input().split()))

possible = [0] * n
possible[0] = 1

for i in range(1, n):
    for j in range(i):
        if possible[j]:
            need = (i - j) * (1 + abs(a[i] - a[j]))
            if need <= k:
                possible[i] = 1
                break

print('YES' if possible[-1] else 'NO')