# https://www.acmicpc.net/problem/1947
MOD = int(1e9)
n = int(input())

a, b = 1, 2
for i in range(3, n):
    a, b = b, (a+b) * i % MOD
print(b if n > 2 else n >> 1)