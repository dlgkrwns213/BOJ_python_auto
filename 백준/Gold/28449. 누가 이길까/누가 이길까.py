# https://www.acmicpc.net/problem/28449
from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
his = sorted(map(int, input().split()))

hi_count = len(his)
win, draw, lose = 0, 0, 0
for arc in map(int, input().split()):
    left = bisect_left(his, arc)
    right = bisect_right(his, arc)

    win += hi_count - right
    draw += right - left
    lose += left

print(win, lose, draw)