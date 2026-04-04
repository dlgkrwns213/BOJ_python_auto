MOD = 10**9 + 7

n, k = map(int, input().split())

a = [0] + [1] * k
for i in range(1, n):
    total = sum(a)
    b = [0] * (k+1)
    for j in range(1, k+1):
        b[j] = total

        for x in range(2*j, k+1, j):
            b[j] -= a[x]
            b[j] %= MOD

    a = b

print(sum(a) % MOD)