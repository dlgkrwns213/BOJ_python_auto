import sys
from itertools import permutations
input = sys.stdin.readline
MAX = int(1e7)


def counting(x):
    made = set()

    length = len(x)
    for i in range(1, length+1):
        for num in permutations(x, i):
            num = int(''.join(num))
            if is_prime[num]:
                made.add(num)

    return len(made)


is_prime = [1] * MAX
is_prime[0], is_prime[1] = 0, 0
for i in range(2, MAX):
    if is_prime[i]:
        for j in range(i+i, MAX, i):
            is_prime[j] = 0

ans = []
for _ in range(int(input())):
    ans.append(counting(input().rstrip()))

print('\n'.join(map(str, ans)))