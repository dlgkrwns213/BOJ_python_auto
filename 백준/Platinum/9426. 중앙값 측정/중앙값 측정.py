import sys
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


def get_mid(node, rest):
    if node >= MAX:
        return node - MAX

    if tree[node << 1] > rest:
        return get_mid(node << 1, rest)
    else:
        return get_mid((node << 1) + 1, rest-tree[node << 1])


n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

# 개수를 저장하는 segment tree
tree = [0] * (MAX << 1)
for num in nums[:k-1]:
    update(num, 1, 0, MAX-1, 1)

total = 0
for i, num in enumerate(nums[k-1:]):
    update(num, 1, 0, MAX-1, 1)
    total += get_mid(0, (k-1) >> 1)
    update(nums[i], -1, 0, MAX-1, 1)

print(total)