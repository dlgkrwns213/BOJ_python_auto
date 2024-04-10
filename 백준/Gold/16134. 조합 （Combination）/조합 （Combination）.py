# https://www.acmicpc.net/problem/16134
MOD = int(1e9)+7


def nCr(n, r):
    N, R = 1, 1
    for i in range(r):
        N = (N*(n-i)) % MOD  # n! / (n-r)!
        R = (R*(r-i)) % MOD  # r!

    inverse_r = pow(R, MOD-2, MOD)  # 1 / r!
    return (N * inverse_r) % MOD  # (n! / (n-r)!) * (1 / r!)


n, r = map(int, input().split())
r = min(r, n-r)
print(nCr(n, r))