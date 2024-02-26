# https://www.acmicpc.net/problem/11689
# 인수의 종류 구하기
def get_prime_factors(num):
    factors = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.add(i)
    if num > 1:
        factors.add(num)
    return sorted(factors)


def backtracking(k, cnt, idx, num, sign):
    global ans
    if cnt == k:
        if sign:
            ans += n // num
        else:
            ans -= n // num
        return

    for i in range(idx, fcnt):
        backtracking(k, cnt+1, i+1, num*factors[i], sign)


n = int(input())

factors = get_prime_factors(n)
if not factors:  # 1과 소수 처리
    if n == 1:
        print(1)
    else:
        print(n-1)
else:
    ans, fcnt = n, len(factors)
    for i in range(fcnt):
        backtracking(i+1, 0, 0, 1, i%2)

    print(ans)