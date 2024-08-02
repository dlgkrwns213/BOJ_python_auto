MAX = int(1e5) + 2


def get_factor_cnt(n):
    factors = []
    for p in primes:
        if p * p > n:
            break

        while not n % p:
            factors.append(p)
            n //= p

    if n > 2:
        factors.append(n)
    return len(factors)


is_prime = [1] * MAX
is_prime[0], is_prime[1] = 0, 0
for i in range(2, MAX):
    if is_prime[i]:
        for j in range(i+i, MAX, i):
            is_prime[j] = 0
primes = [num for num, val in enumerate(is_prime) if val]

a, b = map(int, input().split())
print(sum(map(lambda num: 1 if is_prime[get_factor_cnt(num)] else 0, range(a, b+1))))