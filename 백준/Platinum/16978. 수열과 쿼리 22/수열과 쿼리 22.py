# https://www.acmicpc.net/problem/16978
import sys
from math import ceil, log2


def init(start, last, node):
    if start == last:
        tree[node] = nums[start] if start < n else 0
    else:
        mid = start + last >> 1
        tree[node] = init(start, mid, node << 1) + init(mid+1, last, (node << 1) + 1)
    return tree[node]


def update(idx, diff, start, last, node):
    if idx < start or last < idx:
        return

    tree[node] += diff
    if start < last:
        mid = start + last >> 1
        update(idx, diff, start, mid, node << 1)
        update(idx, diff, mid+1, last, (node << 1) + 1)


def get_sum(left, right, start, last, node):
    if last < left or right < start:
        return 0
    if left <= start and last <= right:
        return tree[node]

    mid = start + last >> 1
    return get_sum(left, right, start, mid, node << 1) + get_sum(left, right, mid+1, last, (node << 1) + 1)


n = int(input())
nums = list(map(int, input().split()))

MAX = 1 << ceil(log2(n))
tree = [0] * (MAX << 1)

init(0, MAX-1, 1)

steps, gets = [], dict()
get_idx = 0
for _ in range(int(input())):
    x, *tmp = map(int, input().split())
    if x == 1:
        steps.append(tmp)
    else:
        k, i, j = tmp
        if k in gets:
            gets[k].append((i, j, get_idx))
        else:
            gets[k] = [(i, j, get_idx)]
        get_idx += 1

ans = [0] * get_idx
step_cnt = len(steps)
for step_idx in range(step_cnt+1):

    if step_idx in gets:
        for i, j, get_idx in gets[step_idx]:
            ans[get_idx] = get_sum(i-1, j-1, 0, MAX-1, 1)

    if step_idx == step_cnt:
        break

    i, v = steps[step_idx]
    update(i-1, v-nums[i-1], 0, MAX-1, 1)
    nums[i-1] = v

print('\n'.join(map(str, ans)))