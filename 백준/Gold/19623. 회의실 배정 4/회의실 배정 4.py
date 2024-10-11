# https://www.acmicpc.net/problem/19623
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
meets = [list(map(int, input().split())) for _ in range(n)]
meets.sort(key=lambda meet: meet[0])

proceeds, finished = [], []

for start, end, people in meets:
    while proceeds and proceeds[0][0] <= start:
        heappush(finished, -heappop(proceeds)[1])

    if finished:
        heappush(proceeds, (end, people + -finished[0]))
    else:
        heappush(proceeds, (end, people))

while proceeds:
    heappush(finished, -heappop(proceeds)[1])

print(-finished[0])