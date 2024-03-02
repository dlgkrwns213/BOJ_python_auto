import sys
from math import ceil, log2
input = sys.stdin.readline


def init(left, right, node):
    if left == right:
        tree[node] = A[left]
    else:
        mid = (left + right) // 2
        tree[node] = init(left, mid, 2*node+1) + init(mid+1, right, 2*node+2)
    return tree[node]


def update_lazy(left, right, node):
    if lazy[node]:
        tree[node] += (right - left + 1) * lazy[node]
        if left != right:
            lazy[node*2+1] += lazy[node]
            lazy[node*2+2] += lazy[node]
        lazy[node] = 0


def update_range(i, j, v, left, right, node):
    update_lazy(left, right, node)
    if right < i or j < left:
        return
    if i <= left and right <= j:
        tree[node] += (right - left + 1) * v
        if left != right:
            lazy[node*2+1] += v
            lazy[node*2+2] += v
        return

    mid = (left + right) // 2
    update_range(i, j, v, left, mid, 2*node+1)
    update_range(i, j, v, mid+1, right, 2*node+2)
    tree[node] = tree[node*2+1] + tree[node*2+2]


def ssum(i, j, left, right, node):
    update_lazy(left, right, node)
    if right < i or j < left:
        return 0
    if i <= left and right <= j:
        return tree[node]

    mid = (left + right) // 2
    return ssum(i, j, left, mid, 2*node+1) + ssum(i, j, mid+1, right, 2*node+2)


n, m, k = map(int, input().split())
A = [int(input()) for _ in range(n)]
size = 2 ** ceil(log2(n))
tree = [0] * (2*size)
lazy = [0] * (2*size)
init(0, n-1, 0)

ans = []
for _ in range(m+k):
    s = input()
    if s[0] == '1':
        _, i, j, v = map(int, s.split())
        update_range(i-1, j-1, v, 0, n-1, 0)
    elif s[0] == '2':
        _, i, j = map(int, s.split())
        ans.append(str(ssum(i-1, j-1, 0, n-1, 0)))

print('\n'.join(ans))