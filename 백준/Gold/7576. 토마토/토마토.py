import sys
from collections import deque


def solve():
    def bfs():
        go = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while que:
            p, q, count = que.popleft()
            day.append(count)

            for x, y in go:
                pp, qq = p+x, q+y
                if pp<0 or pp>=n or qq<0 or qq>=m:
                    continue
                if visited[pp][qq] or box[pp][qq]==1:
                    continue

                visited[pp][qq] = True
                que.append([pp, qq, count+1])


    input = sys.stdin.readline
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    que, day = deque(), [0]
    for i, line in enumerate(box):
        for j, v in enumerate(line):
            if v==1:
                que.append([i, j, 0])
                visited[i][j] = True
            elif v==-1:
                visited[i][j] = True

    bfs()

    all_visit = True
    for line in visited:
        for tf in line:
            if not tf:
                all_visit = False
                break

    if not all_visit:
        print(-1)
    else:
        print(day[-1])

if __name__ == '__main__':
    solve()