MOD = int(1e9) + 7

n = int(input())

a, b = 1, 1
for i in range(2, n):
    a, b = b, (a+b) % MOD

print(b, n-2)