# https://www.acmicpc.net/problem/1306
from math import ceil, log2


def init(start, last, node):
    if start == last:
        tree[node] = lights[start]
    else:
        mid = start + last >> 1
        tree[node] = max(init(start, mid, node << 1), init(mid+1, last, (node << 1) + 1))
    return tree[node]


def get_max(start, last, left, right, node):
    if last < left or right < start:
        return 0
    if left <= start and last <= right:
        return tree[node]

    mid = start + last >> 1
    return max(get_max(start, mid, left, right, node << 1), get_max(mid+1, last, left, right, (node << 1) + 1))


n, m = map(int, input().split())
lights = list(map(int, input().split()))

MAX = 1 << (ceil(log2(n+1)))
tree = [0] * (MAX << 1)

init(0, n-1, 1)
ans = list(map(lambda idx: get_max(0, n-1, idx-m+1, idx+m-1, 1), range(m-1, n-m+1)))

print(' '.join(map(str, ans)))