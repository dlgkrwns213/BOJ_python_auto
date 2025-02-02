# https://www.acmicpc.net/problem/20440
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
times = defaultdict(int)
for _ in range(n):
    e, x = map(int, input().split())
    times[e] += 1
    times[x] -= 1

sorted_times = sorted([time for time in times.items() if time[1]])

mx, mx_idx, now = 0, -1, 0
for idx, time in enumerate(sorted_times):
    t, c = time
    now += c
    if mx < now:
        mx, mx_idx = now, idx

print(mx)
print(sorted_times[mx_idx][0], sorted_times[mx_idx+1][0])