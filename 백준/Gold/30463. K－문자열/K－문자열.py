# https://www.acmicpc.net/problem/30463
import sys
input = sys.stdin.readline


def get_bit(x: str):
    bit = 0
    for a in map(int, x):
        bit |= 1 << a
    return bit


def find(x):
    cnt = 0
    for i in range(10):
        if (1 << i) & x:
            cnt += 1
    return cnt


n, k = map(int, input().split())
counts = [0] * 1024
for _ in range(n):
    counts[get_bit(input().rstrip())] += 1

total = 0
for i in range(1024):
    if find(i) == k:
        total += counts[i] * (counts[i]-1) >> 1
    for j in range(i+1, 1024):
        if find(i | j) == k:
            total += counts[i] * counts[j]
print(total)