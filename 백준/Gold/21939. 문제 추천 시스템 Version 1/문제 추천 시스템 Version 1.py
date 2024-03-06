# https://www.acmicpc.net/problem/21939
import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

n = int(input())
mn_hq, mx_hq = [], []
level = [0] * 100001
for _ in range(n):
    p, l = map(int, input().split())
    heappush(mn_hq, (l, p))
    heappush(mx_hq, (-l, -p))
    level[p] = l

ans = []
for _ in range(int(input())):
    command, *tmp = input().split()
    tmp = map(int, tmp)
    if command == 'recommend':
        [x] = tmp
        if x == 1:
            while 1:
                l, p = mx_hq[0]
                if level[-p] == -l:
                    ans.append(-p)
                    break
                heappop(mx_hq)
        else:
            while 1:
                l, p = mn_hq[0]
                if level[p] == l:
                    ans.append(p)
                    break
                heappop(mn_hq)

    elif command == 'add':
        p, l = tmp
        heappush(mn_hq, (l, p))
        heappush(mx_hq, (-l, -p))
        level[p] = l
    else:
        [p] = tmp
        level[p] = 0

print('\n'.join(map(str, ans)))