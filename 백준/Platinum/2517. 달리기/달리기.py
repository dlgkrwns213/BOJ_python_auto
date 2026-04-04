import sys

input = sys.stdin.readline


def update(i):
    while i <= n:
        tree[i] += 1
        i += i & -i


def query(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s


n = int(input())
abilities = [(int(input()), i) for i in range(n)]
abilities.sort(reverse=True)

tree = [0] * (n+1)
result = [0] * n

for ability, idx in abilities:
    cnt = query(idx)
    result[idx] = cnt+1
    update(idx+1)

print('\n'.join(map(str, result)))