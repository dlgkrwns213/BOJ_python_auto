import sys
from math import ceil, log2
input = sys.stdin.readline


def init(start, last, tree, node, odd_even):
    if start == last:
        tree[node] = (A[start]+odd_even) % 2
    else:
        mid = (start + last) // 2
        init(start, mid, tree, 2*node+1, odd_even)
        init(mid+1, last, tree, 2*node+2, odd_even)
        tree[node] = tree[2*node+1] + tree[2*node+2]


def update(idx, val, start, last, tree, node, odd_even):
    if idx < start or last < idx:
        return tree[node]
    if start == last:
        tree[node] = (val + odd_even) % 2
    else:
        mid = (start + last) // 2
        tree[node] = update(idx, val, start, mid, tree, 2*node+1, odd_even) + update(idx, val, mid+1, last, tree, 2*node+2, odd_even)
    return tree[node]


def ssum(i, j, start, last, tree, node):
    if last < i or j < start:
        return 0
    if i <= start and last <= j:
        return tree[node]

    mid = (start + last) // 2
    return ssum(i, j, start, mid, tree, 2*node+1) + ssum(i, j, mid+1, last, tree, 2*node+2)


n = int(input())
A = list(map(int, input().split()))
size = 2 ** ceil(log2(n))
odd_tree = [0] * (2*size)
even_tree = [0] * (2*size)
init(0, n-1, odd_tree, 0, 0)
init(0, n-1, even_tree, 0, 1)

for _ in range(int(input())):
    s, a, b = map(int, input().split())
    if s == 1:
        update(a-1, b, 0, n-1, odd_tree, 0, 0)
        update(a-1, b, 0, n-1, even_tree, 0, 1)
    elif s == 2:
        print(ssum(a-1, b-1, 0, n-1, even_tree, 0))
    else:
        print(ssum(a-1, b-1, 0, n-1, odd_tree, 0))