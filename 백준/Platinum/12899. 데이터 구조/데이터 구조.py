# https://www.acmicpc.net/problem/12899
import sys
input = sys.stdin.readline
MAX = 1 << 21


def update(node, val):
    while node:
        tree[node] += val
        node >>= 1


def get_xth(node, rest):
    if node >= MAX:
        return node - MAX

    if tree[node << 1] >= rest:
        if tree[node << 1] == rest and not tree[node << 1]:
            return get_xth(node << 1 | 1, rest - tree[node << 1])
        return get_xth(node << 1, rest)
    else:
        return get_xth(node << 1 | 1, rest - tree[node << 1])


tree = [0] * (MAX << 1)
ans = []
for _ in range(int(input())):
    t, x = map(int, input().split())
    if t == 1:
        update(x+MAX, 1)
    else:
        num = get_xth(1, x)
        ans.append(num)
        update(num+MAX, -1)

print('\n'.join(map(str, ans)))