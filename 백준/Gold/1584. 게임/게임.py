from collections import deque
import sys
input = sys.stdin.readline


def making(num):
    x1, y1, x2, y2 = ipt
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y2, y1 = y1, y2
    
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            area[i][j] = num
            

def zero_one_bfs():
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    q = deque()
    q.append((0, 0, 0))
    
    visited = [[False]*501 for _ in range(501)]
    visited[0][0] = True
    
    while q:
        x, y, lost = q.popleft()
        if x==500 and y==500:
            return lost
        
        for a, b in go:
            pp, qq = x+a, y+b
            if pp < 0 or pp > 500 or qq < 0 or qq > 500:
                continue
            if visited[pp][qq]:
                continue
            if area[pp][qq] == 2:
                continue
            
            visited[pp][qq] = True
            if not area[pp][qq]:
                q.appendleft((pp, qq, lost))
            else:
                q.append((pp, qq, lost+1))
    
    return -1       
        
            
area = [[0]*501 for _ in range(501)]
for n in range(2):
    for _ in range(int(input())):
        ipt = list(map(int, input().split()))
        making(n+1)

print(zero_one_bfs())