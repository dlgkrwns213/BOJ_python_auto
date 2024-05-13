# https://www.acmicpc.net/problem/1344
a = int(input())
b = int(input())

primes = [2, 3, 5, 7, 11, 13, 17]
a_total, b_total = 0, 0
for prime in primes:
    n, r = 1, 1
    for i in range(min(prime, 18-prime)):
        n *= 18 - i
        r *= i + 1

    x = n // r
    a_total += a ** prime * (100-a) ** (18-prime) * x
    b_total += b ** prime * (100-b) ** (18-prime) * x

pa, pb = a_total / 100 ** 18, b_total / 100 ** 18
print(1 - (1-pa) * (1-pb))