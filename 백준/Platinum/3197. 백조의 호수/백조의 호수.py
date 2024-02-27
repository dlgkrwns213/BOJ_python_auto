import sys
from collections import deque
input = sys.stdin.readline


# 얼음의 높이 구하기 (하루 늦게 녹음 -> 높이가 1 높음)
def get_ice_height():
    q = deque()
    
    for i in range(r):
        for j in range(c):
            if lake[i][j] == 'X':
                height[i][j] = -1
                for a, b in go:
                    pp, qq = i+a, j+b
                    if pp < 0 or pp >= r or qq < 0 or qq >= c:
                        continue
                    if lake[pp][qq] == '.':
                        height[i][j] = 1
                        q.append((i, j, 1))
                        break
                
    while q:
        x, y, h = q.popleft()
        
        for a, b in go:
            pp, qq = x+a, y+b
            if pp < 0 or pp >= r or qq < 0 or qq >= c:
                continue
            if height[pp][qq] != -1:
                continue
                
            height[pp][qq] = h+1
            q.append((pp, qq, h+1))


# 01bfs: 오늘(이전 포함) 갈수 있으면 0, 바로 내일 갈수 있으면 1
def bfs():
    q = deque()
    q.append((s1, s2, 0))
    
    visited = [[False]*c for _ in range(r)]
    visited[s1][s2] = True
    
    while q:
        x, y, h = q.popleft()
        if (x, y) == (d1, d2):
            return h
        
        for a, b in go:
            pp, qq = x+a, y+b
            if pp < 0 or pp >= r or qq < 0 or qq >= c:
                continue
            if visited[pp][qq]:
                continue
                
            visited[pp][qq] = True
            if height[pp][qq] <= h:
                q.appendleft((pp, qq, h))
            elif height[pp][qq] == h+1:
                q.append((pp, qq, h+1))


go = ((-1, 0), (1, 0), (0, 1), (0, -1))
r, c = map(int, input().split())
lake = [[x for x in input().rstrip()] for _ in range(r)]

swan = []
for i in range(r):
    for j in range(c):
        if lake[i][j] == 'L':
            lake[i][j] = '.'
            swan.extend((i, j))
            
height = [[0]*c for _ in range(r)]
get_ice_height()

s1, s2, d1, d2 = swan
print(bfs())