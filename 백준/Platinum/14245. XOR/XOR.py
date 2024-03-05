# https://www.acmicpc.net/problem/14245
import sys
from math import ceil, log2
input = sys.stdin.readline


def init(start, last, node):
    if start == last:
        tree[node] = nums[start] if start < n else 0
    else:
        mid = start + last >> 1
        tree[node] = init(start, mid, node << 1) ^ init(mid+1, last, node << 1 | 1)
    return tree[node]


def lazy_propagation(start, last, node):
    if lazy[node]:
        tree[node] ^= 0 if (last - start) % 2 else lazy[node]
        if start < last:
            lazy[node << 1] ^= lazy[node]
            lazy[node << 1 | 1] ^= lazy[node]
        lazy[node] = 0


def update_range(left, right, val, start, last, node):
    lazy_propagation(start, last, node)
    if last < left or right < start:
        return tree[node]

    if left <= start and last <= right:
        tree[node] ^= 0 if (last - start) % 2 else val
        if start < last:
            lazy[node << 1] ^= val
            lazy[node << 1 | 1] ^= val
    else:
        mid = start + last >> 1
        l_child = update_range(left, right, val, start, mid, node << 1)
        r_child = update_range(left, right, val, mid+1, last, node << 1 | 1)
        tree[node] = l_child ^ r_child

    return tree[node]


def get_xor(idx, start, last, node):
    lazy_propagation(start, last, node)
    if idx < start or last < idx:
        return 0
    if start == last:
        return tree[node]

    mid = start + last >> 1
    l_child = get_xor(idx, start, mid, node << 1)
    r_child = get_xor(idx, mid+1, last, node << 1 | 1)
    return l_child ^ r_child


n = int(input())
nums = list(map(int, input().split()))

MAX = 1 << ceil(log2(n))
tree = [0] * (MAX << 1)

init(0, MAX-1, 1)

lazy = [0] * (MAX << 1)
ans = []
for _ in range(int(input())):
    x, *tmp = map(int, input().split())
    if x == 1:
        a, b, c = tmp
        update_range(a, b, c, 0, MAX-1, 1)
    else:
        [b] = tmp
        ans.append(get_xor(b, 0, MAX-1, 1))

print('\n'.join(map(str, ans)))