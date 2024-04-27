# https://www.acmicpc.net/problem/1153
MAX = int(1e6)


def prime_checking():
    is_prime = [True] * MAX
    is_prime[0], is_prime[1] = False, False

    for i in range(2, MAX):
        if is_prime[i]:
            for j in range(i+i, MAX, i):
                is_prime[j] = False

    return is_prime


n = int(input())
if n < 8:
    print(-1)
else:
    is_prime = prime_checking()

    if n % 2:
        n -= 5
        ans = [2, 3]
    else:
        n -= 4
        ans = [2, 2]

    for i in range(2, MAX):
        if is_prime[i] and is_prime[n-i]:
            ans += [i, n-i]
            break

    print(*ans)