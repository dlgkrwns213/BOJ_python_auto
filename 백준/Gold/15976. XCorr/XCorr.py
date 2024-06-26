# https://www.acmicpc.net/problem/15976
import sys
from copy import deepcopy
input = sys.stdin.readline
INF = float('inf')


def bisect_right(find_idx):
    left, right = 0, m+1
    while left < right:
        mid = left + right >> 1
        if prefix_y[mid][0] >= find_idx:
            right = mid
        else:
            left = mid + 1

    return prefix_y[left-1][1]


def bisect_left(find_idx):
    left, right = 0, m+1
    while left < right:
        mid = left + right >> 1
        if prefix_y[mid][0] >= find_idx:
            right = mid
        else:
            left = mid + 1

    if prefix_y[left][0] != find_idx:
        left -= 1
    return prefix_y[left][1]


n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
y = [list(map(int, input().split())) for _ in range(m)]
a = int(input())
b = int(input())

prefix_y = deepcopy(y)
for i in range(1, m):
    prefix_y[i][1] += prefix_y[i-1][1]
prefix_y = [[-INF, 0]] + prefix_y + [[INF, INF]]

### O(N * M) 방식
# total = 0
# for idx_x, num_x in x:
#     # idx+a ~ idx+b 까지의 합을 구해야 함
#     sum_y = 0
#     for idx_y, num_y in y:
#         if idx_x + a <= idx_y <= idx_x + b:
#             sum_y += num_y
#     total += sum_y * num_x

total = 0
for idx_x, num_x in x:
    sum_y = bisect_left(idx_x+b) - bisect_right(idx_x+a)
    total += sum_y * num_x

print(total)