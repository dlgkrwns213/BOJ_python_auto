# https://www.acmicpc.net/problem/3078
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
cnt, q, total = [0] * 21, deque(), 0
for i in range(n):
    length = len(input().rstrip())
    total += cnt[length]

    if i >= k:
        cnt[q.popleft()] -= 1

    cnt[length] += 1
    q.append(length)

print(total)