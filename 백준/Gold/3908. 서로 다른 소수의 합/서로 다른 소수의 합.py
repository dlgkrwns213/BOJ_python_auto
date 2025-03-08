# https://www.acmicpc.net/problem/3908
import sys
input = sys.stdin.readline
MAX = 1121

is_prime = [1] * MAX
is_prime[0], is_prime[1] = 0, 0
for i in range(2, MAX):
    if is_prime[i]:
        for j in range(i+i, MAX, i):
            is_prime[j] = 0
primes = [num for num in range(MAX) if is_prime[num]]

dp = [[0]*MAX for _ in range(15)]
dp[0][0] = 1
for prime in primes:
    for num in range(MAX-1, prime-1, -1):
        for k in range(1, 15):
            dp[k][num] += dp[k-1][num-prime]

ans = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    ans.append(dp[k][n])
print('\n'.join(map(str, ans)))