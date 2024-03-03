# https://www.acmicpc.net/problem/10868
import sys
from math import ceil, log2
input = sys.stdin.readline
INF = sys.maxsize


def init(left, right, idx):
    if left == right:
        tree[idx] = nums[left]
    else:
        mid = left + right >> 1
        tree[idx] = min(init(left, mid, 2*idx+1), init(mid+1, right, 2*idx+2))
    return tree[idx]


def get_min(x, y, left, right, idx):
    if right < x or y < left:
        return INF
    if x <= left and right <= y:
        return tree[idx]

    mid = left + right >> 1
    return min(get_min(x, y, left, mid, 2*idx+1), get_min(x, y, mid+1, right, 2*idx+2))


n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]

size = 1 << ceil(log2(n)) + 1
tree = [0] * size
init(0, n-1, 0)

ans = [0] * m
for i in range(m):
    a, b = map(lambda num: int(num)-1, input().split())
    ans[i] = get_min(a, b, 0, n-1, 0)

print('\n'.join(map(str, ans)))