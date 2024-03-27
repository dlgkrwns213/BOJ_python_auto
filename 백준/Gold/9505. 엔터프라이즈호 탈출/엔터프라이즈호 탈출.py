# https://www.acmicpc.net/problem/9505
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')


def init():

    start, board = -1, [0] * h * w
    idx = 0
    for _ in range(h):
        for v in input().rstrip():
            if v != 'E':
                board[idx] = fight_times[v]
            else:
                start = idx
            idx += 1

    return start, board


def dijkstra():
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))

    times = [INF] * h * w
    times[start] = 0

    hq = []
    heappush(hq, (0, start))

    mn = INF
    while hq:
        time, xy = heappop(hq)
        if times[xy] < time:
            continue

        x, y = divmod(xy, w)
        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                mn = min(mn, time)
                continue

            nxy = nx*w+ny
            nxt_time = board[nxy] + time
            if times[nxy] > nxt_time:
                times[nxy] = nxt_time
                heappush(hq, (nxt_time, nxy))

    return mn


ans = []
for _ in range(int(input())):
    k, w, h = map(int, input().split())
    fight_times = dict()
    for _ in range(k):
        spaceship, time = input().split()
        fight_times[spaceship] = int(time)

    start, board = init()

    ans.append(dijkstra())

print('\n'.join(map(str, ans)))