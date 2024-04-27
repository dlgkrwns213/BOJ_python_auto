import sys
input = sys.stdin.readline


def is_prime(num):
    for i in range(2, int(num ** 0.5)+1):
        if not num % i:
            return False
    return True


ans = []
while True:
    p, a = map(int, input().split())
    if not p and not a:
        break

    if not is_prime(p) and pow(a, p, p) == a:
        ans.append(True)
    else:
        ans.append(False)

print('\n'.join(map(lambda x: 'yes' if x else 'no', ans)))