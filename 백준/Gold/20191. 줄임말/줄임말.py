# https://www.acmicpc.net/problem/20191
from bisect import bisect_left, bisect_right
integer = lambda alpha: ord(alpha) - ord('a')
INF = float('inf')

s = input()
t = input()

indexes = [[] for _ in range(26)]
for i, x in enumerate(t):
    indexes[integer(x)].append(i)
for index in indexes:
    index.append(INF)

cnt, idx = 1, -1
for x in s:
    xi = integer(x)
    index = indexes[xi]
    if len(index) == 1:
        cnt = 0
        idx = -1
        break
    if index[-2] < idx:
        cnt += 1
        idx = -1

    idx = index[bisect_right(index, idx)]
    if idx == INF:
        idx = index[bisect_right(index, -1)]
        cnt += 1

print(cnt - (1 if idx == -1 else 0))