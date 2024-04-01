# https://www.acmicpc.net/problem/14848
from math import lcm


def backtracking(cnt, idx, num):
    global total
    if idx == k:
        total += (n // num) * (-1 if cnt % 2 else 1)
        return

    backtracking(cnt, idx+1, num)
    backtracking(cnt+1, idx+1, lcm(num, A[idx]))


n, k = map(int, input().split())
A = list(map(int, input().split()))

total = 0
backtracking(0, 0, 1)
print(total)