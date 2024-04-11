# https://www.acmicpc.net/problem/11014
import sys
input = sys.stdin.readline


def get_graph(classroom: list[str]):
    get_idx = lambda x, y: x * m + y
    see = ((-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 1))

    empty = sum(map(lambda line: line.count('x'), classroom))
    graph = [[] for _ in range(n*m)]

    for i in range(n):
        for j in range(m):
            if classroom[i][j] == 'x':
                continue

            now = get_idx(i, j)
            for a, b in see:
                ni, nj = i + a, j + b
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                if classroom[ni][nj] == 'x':
                    continue
                nxt = get_idx(ni, nj)

                graph[now].append(nxt)

    return empty, graph


def dfs(cheater):
    if visited[cheater]:
        return False
    visited[cheater] = True

    for cheated in graph[cheater]:
        if matched[cheated] == -1:
            matched[cheated] = cheater
            return True
    for cheated in graph[cheater]:
        if dfs(matched[cheated]):
            matched[cheated] = cheater
            return True
    return False


ans = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    empty, graph = get_graph([input().rstrip() for _ in range(n)])

    matched = [-1] * (n * m)
    for x in range(n*m):
        visited = [False] * (n * m)
        dfs(x)

    max_connect = n * m - matched.count(-1)
    ans.append(n * m - empty - max_connect // 2)

print('\n'.join(map(str, ans)))