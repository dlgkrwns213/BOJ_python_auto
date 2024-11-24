MOD = 123456789

n = int(input())

is_prime = [1] * (n+1)
is_prime[0], is_prime[1] = 0, 0
for i in range(2, n+1):
    if is_prime[i]:
        for j in range(i+i, n+1, i):
            is_prime[j] = 0

primes = [num for num in range(2, n+1) if is_prime[num]]
dp = [0] * (n+1)
dp[0] = 1
for prime in primes:
    for i in range(prime, n+1):
        dp[i] += dp[i-prime]
        dp[i] %= MOD

print(dp[n])