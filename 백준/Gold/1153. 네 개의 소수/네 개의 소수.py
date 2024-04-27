# https://www.acmicpc.net/problem/1153
MAX = int(1e6)


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True


n = int(input())
if n < 8:
    print(-1)
else:
    if n % 2:
        n -= 5
        ans = [2, 3]
    else:
        n -= 4
        ans = [2, 2]

    for i in range(2, MAX):
        if is_prime(i) and is_prime(n-i):
            ans += [i, n-i]
            break

    print(*ans)