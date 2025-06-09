MAX = 120
is_prime = [1] * MAX
is_prime[0], is_prime[1] = 0, 0
for i in range(2, MAX):
    if is_prime[i]:
        for j in range(i+i, MAX, i):
            is_prime[j] = 0

primes = [number for number in range(MAX) if is_prime[number]]
can_make = [0] * 240
for prime1 in primes:
    for prime2 in primes:
        can_make[prime1+prime2] = 1

print('\n'.join(map(lambda x: 'Yes' if can_make[x] else 'No', (int(input()) for _ in range(int(input()))))))