### https://www.acmicpc.net/problem/1572
import sys
from collections import deque
input = sys.stdin.readline
MAX = 1 << 16


def update(idx, val, start, last, node):
    if idx < start or last < idx:
        return

    tree[node] += val
    if start < last:
        mid = start + last >> 1
        update(idx, val, start, mid, node << 1)
        update(idx, val, mid+1, last, (node << 1) + 1)


def find_middle(node, rest):
    if node >= MAX:
        return node - MAX

    if tree[node << 1] > rest:
        return find_middle(node << 1, rest)
    else:
        return find_middle((node << 1) + 1, rest - tree[node << 1])

n, k = map(int, input().split())

tree, q, mx_cnt = [0] * (MAX << 1), deque(), 0
for _ in range(k-1):
    num = int(input())
    q.append(num)
    if num == MAX:
        mx_cnt += 1
    else:
        update(num, 1, 0, MAX-1, 1)

total = 0
for _ in range(k-1, n):
    num = int(input())
    q.append(num)
    if num == MAX:
        mx_cnt += 1
    else:
        update(num, 1, 0, MAX-1, 1)

    if mx_cnt > k >> 1:
        middle = MAX
    else:
        middle = find_middle(1, (k-1) // 2)
    total += middle

    delete = q.popleft()
    if delete == MAX:
        mx_cnt -= 1
    else:
        update(delete, -1, 0, MAX-1, 1)

print(total)