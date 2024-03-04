# https://www.acmicpc.net/problem/16978
import sys
from math import ceil, log2
input = sys.stdin.readline


def init(start, last, node):
    if start == last:
        tree[node] = (nums[start], 0) if start < n else (0, 0)
    else:
        mid = start + last >> 1
        left1, left2 = init(start, mid, node << 1)
        right1, right2 = init(mid+1, last, (node << 1) + 1)

        if left2 > right1:
            tree[node] = (left1, left2)
        elif right2 > left1:
            tree[node] = (right1, right2)
        else:
            tree[node] = (max(left1, right1), min(left1, right1))

    return tree[node]


def update(idx, val, start, last, node):
    if idx < start or last < idx:
        return tree[node]

    if start == last:
        tree[node] = (val, 0)
    else:
        mid = start + last >> 1
        left1, left2 = update(idx, val, start, mid, node << 1)
        right1, right2 = update(idx, val, mid+1, last, (node << 1) + 1)

        if left2 > right1:
            tree[node] = (left1, left2)
        elif right2 > left1:
            tree[node] = (right1, right2)
        else:
            tree[node] = (max(left1, right1), min(left1, right1))

    return tree[node]


def get_max(left, right, start, last, node):
    if last < left or right < start:
        return 0, 0
    if left <= start and last <= right:
        return tree[node]

    mid = start + last >> 1
    left1, left2 = get_max(left, right, start, mid, node << 1)
    right1, right2 = get_max(left, right, mid+1, last, (node << 1) + 1)

    if left2 > right1:
        return left1, left2
    elif right2 > left1:
        return right1, right2
    else:
        return max(left1, right1), min(left1, right1)


n = int(input())
nums = list(map(int, input().split()))

MAX = 1 << ceil(log2(n))
tree = [() for _ in range(MAX << 1)]

init(0, MAX-1, 1)

ans = []
for _ in range(int(input())):
    x, a, b = map(int, input().split())
    if x == 1:
        update(a-1, b, 0, MAX-1, 1)
    else:
        ans.append(sum(get_max(a-1, b-1, 0, MAX-1, 1)))

print('\n'.join((map(str, ans))))