import sys
from collections import deque
input = sys.stdin.readline
go = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs(x, y):    
    q = deque()
    q.append((x, y, 0))

    height = [[-1]*(w) for _ in range(h)]
    height[x][y] = 0
    
    while q:
        x, y, hi = q.popleft()
        
        for a, b in go:
            pp, qq = x+a, y+b
            if pp < 0 or pp >= h or qq < 0 or qq >= w:
                continue
            if prison[pp][qq] == '*':
                continue
            if height[pp][qq] != -1:
                continue
                
            if prison[pp][qq] == '.':
                height[pp][qq] = hi
                q.appendleft((pp, qq, hi))
            elif prison[pp][qq] == '#':
                height[pp][qq] = hi+1
                q.append((pp, qq, hi+1))

    return height
        
        
for _ in range(int(input())):
    h, w = map(int, input().split())
    prison = [['.']*(w+2)] + [['.'] + [x for x in input().rstrip()] + ['.'] for _ in range(h)] + [['.']*(w+2)]
    h, w = h+2, w+2
    
    prisoner = []
    for i in range(h):
        for j in range(w):
            if prison[i][j] == '$':
                prisoner.extend((i, j))
                prison[i][j] = '.'
    
    out = bfs(0, 0)
    one = bfs(prisoner[0], prisoner[1])
    two = bfs(prisoner[2], prisoner[3])
    
    m = 10**9
    for i in range(h):
        for j in range(w):
            now = one[i][j] + two[i][j] + out[i][j]
            if prison[i][j] == '*' or one[i][j] == -1:
                continue
            
            if prison[i][j] == '#':
                now -= 2
            m = min(m, now)
    print(m)
    