# https://www.acmicpc.net/problem/1168
from math import ceil, log2


def init(start, last, node):
    if start == last:
        tree[node] = 1 if start < n else 0
    else:
        mid = start + last >> 1
        tree[node] = init(start, mid, node << 1) + init(mid+1, last, (node << 1) + 1)
    return tree[node]


def update(idx, val, start, last, node):
    if idx < start or last < idx:
        return

    tree[node] += val
    if start < last:
        mid = start + last >> 1
        update(idx, val, start, mid, node << 1)
        update(idx, val, mid+1, last, (node << 1) + 1)


def find(node, rest):
    if node >= MAX:
        return node - MAX

    if tree[node << 1] >= rest:
        if tree[node << 1] == rest and not tree[node << 1]:
            return find((node << 1) + 1, rest - tree[node << 1])
        return find(node << 1, rest)
    else:
        return find((node << 1) + 1, rest - tree[node << 1])


n, m = map(int, input().split())

MAX = 1 << ceil(log2(n+1))
tree = [0] * (MAX << 1)

init(0, MAX-1, 1)

now, ans = 1, []
for _ in range(n):
    nxt = (now + m - 1) % tree[1]
    if not nxt:
        nxt = tree[1]

    num = find(1, nxt)
    ans.append(num)
    update(num, -1, 0, MAX-1, 1)

    now = nxt

print(f'<{", ".join(map(lambda x: str(x+1), ans))}>')