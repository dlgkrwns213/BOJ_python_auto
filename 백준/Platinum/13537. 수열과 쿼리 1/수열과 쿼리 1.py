import sys
from math import ceil, log2
input = sys.stdin.readline


def update(idx, val, start, last, node):
    if idx < start or last < idx:
        return
    tree[node].append(val)
    if start < last:
        mid = (start + last) // 2
        update(idx, val, start, mid, 2*node+1)
        update(idx, val, mid+1, last, 2*node+2)


def query(left, right, start, last, val, node):
    if last < left or right < start:
        return 0
    if left <= start and last <= right:
        return len(tree[node]) - upper_bound(tree[node], val)
    mid = (start + last) // 2
    return query(left, right, start, mid, val, 2*node+1) + query(left, right, mid+1, last, val, 2*node+2)


def upper_bound(nums, val):
    start, last = 0, len(nums)
    while start < last:
        mid = (start + last) // 2
        if nums[mid] <= val:
            start = mid + 1
        else:
            last = mid
    return last


n = int(input())
A = list(map(int, input().split()))
size = 2 ** ceil(log2(n)+1)
tree = [[] for _ in range(size)]

for i in range(n):
    update(i, A[i], 0, n-1, 0)
for i in range(size):
    tree[i].sort()

for _ in range(int(input())):
    i, j, v = map(int, input().split())
    print(query(i-1, j-1, 0, n-1, v, 0))