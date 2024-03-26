# https://www.acmicpc.net/problem/1379
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures.sort(key=lambda lecture: lecture[1])

hq, rest, classrooms = [], [], [0] * n
for lecture_idx, start, end in lectures:
    while hq and hq[0][0] <= start:
        _, classroom_idx = heappop(hq)
        heappush(rest, classroom_idx)

    ci = len(hq) + 1
    if rest:
        ci = heappop(rest)

    heappush(hq, (end, ci))
    classrooms[lecture_idx-1] = ci

print(max(classrooms))
print('\n'.join(map(str, classrooms)))