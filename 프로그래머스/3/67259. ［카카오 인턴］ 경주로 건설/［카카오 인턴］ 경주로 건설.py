from heapq import heappush, heappop

def solution(board):
    def dijkstra():
        go = ((-1, 0), (1, 0), (0, -1), (0, 1))
        INF = float('inf')
        
        distances = [[[INF]*4 for _ in range(m)] for _ in range(n)]
        distances[0][0] = [0] * 4
        
        hq = []
        heappush(hq, (-500, 0, 0, 4))
        
        while hq:
            dist, x, y, di = heappop(hq)
            if (x, y) != (0, 0) and distances[x][y][di] < dist:
                continue
                
            for nxt_di, direction in enumerate(go):
                a, b = direction
                nx, ny = x+a, y+b
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if board[nx][ny]:
                    continue
                
                nxt_dist = dist + (100 if di == nxt_di else 600)
                if distances[nx][ny][nxt_di] >= nxt_dist:
                    distances[nx][ny][nxt_di] = nxt_dist
                    heappush(hq, (nxt_dist, nx, ny, nxt_di))
                    
        for line in distances:
            print(line)
        return min(distances[-1][-1])
        
    n, m = map(len, (board, board[0]))
    return dijkstra()