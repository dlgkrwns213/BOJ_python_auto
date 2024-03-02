# https://www.acmicpc.net/problem/2243
import sys
input = sys.stdin.readline
MAX = 1 << 20


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
            return find((node << 1) + 1, rest-tree[node << 1])
        return find((node << 1), rest)
    elif tree[node << 1] < rest:
        return find((node << 1) + 1, rest - tree[node << 1])


n = int(input())
tree = [0] * (MAX << 1)
ans = []
for _ in range(n):
    a, *tmp = map(int, input().split())
    if a == 1:
        [b] = tmp
        x = find(1, b)
        ans.append(x)
        update(x, -1, 0, MAX-1, 1)
    else:
        b, c = tmp
        update(b, c, 0, MAX-1, 1)

print('\n'.join(map(str, ans)))