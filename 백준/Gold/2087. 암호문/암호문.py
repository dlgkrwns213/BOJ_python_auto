# https://www.acmicpc.net/problem/17305
import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
want = int(input())

left = n >> 1
make = {}
for i in range(1 << left):
    subset = tuple(j for j in range(n) if (i >> j) & 1)
    make[sum(map(lambda x: numbers[x], subset))] = subset

right = n - left
for i in range(1 << right):
    subset = tuple(j+left for j in range(n) if (i >> j) & 1)
    find = want - sum(map(lambda x: numbers[x], subset))
    if find in make:
        answer_number = make[find] + subset
        print(''.join(map(lambda x: '1' if x in answer_number else '0', range(n))))
        break