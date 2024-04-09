# https://www.acmicpc.net/problem/3683
import sys
input = sys.stdin.readline


def get_graph(votes: list[(str, str)]):
    graph = [[] for _ in range(v)]
    for i in range(v):
        like_i, hate_i = votes[i]
        for j in range(i+1, v):
            like_j, hate_j = votes[j]

            if like_i == hate_j or hate_i == like_j:
                graph[i].append(j)
                graph[j].append(i)

    return graph


def dfs(now):
    if visited[now]:
        return False
    visited[now] = True

    for cont in graph[now]:
        if matched[cont] == -1:
            matched[cont] = now
            return True
    for cont in graph[now]:
        if dfs(matched[cont]):
            matched[cont] = now
            return True
    return False


ans = []
for _ in range(int(input())):
    _, _, v = map(int, input().split())

    graph = get_graph([tuple(input().split()) for _ in range(v)])

    matched = [-1] * v
    for i in range(v):
        visited = [False] * v
        dfs(i)

    ans.append(v + matched.count(-1) >> 1)

print('\n'.join(map(str, ans)))