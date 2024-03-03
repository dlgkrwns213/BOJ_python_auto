import sys
from math import ceil, log2
input = sys.stdin.readline


def init(left, right, idx):
    if left == right:
        tree[idx] = A[left]
    else:
        mid = (left + right) // 2
        tree[idx] = init(left, mid, 2*idx+1) + init(mid+1, right, 2*idx+2)
    return tree[idx]


def update(idx, val, left, right, tree_idx):
    if idx < left or right < idx:
        return tree[tree_idx]

    if left == right:
        tree[tree_idx] = val
    else:
        mid = (left + right) // 2
        tree[tree_idx] = update(idx, val, left, mid, 2*tree_idx+1) + update(idx, val, mid+1, right, 2*tree_idx+2)
    return tree[tree_idx]


def ssum(i, j, left, right, tree_idx):
    if right < i or j < left:
        return 0
    if i <= left and right <= j:
        return tree[tree_idx]

    mid = (left + right) // 2
    return ssum(i, j, left, mid, 2*tree_idx+1) + ssum(i, j, mid+1, right, 2*tree_idx+2)


n, m = map(int, input().split())
A = list(map(int, input().split()))
tree = [0] * (2 ** ((ceil(log2(n)))+1))
init(0, n-1, 0)

ans = [0] * m
for i in range(m):
    x, y, a, b = map(int, input().split())
    x, y = min(x, y), max(x, y)
    ans[i] = str(ssum(x-1, y-1, 0, n-1, 0))
    update(a-1, b, 0, n-1, 0)

print('\n'.join(ans))