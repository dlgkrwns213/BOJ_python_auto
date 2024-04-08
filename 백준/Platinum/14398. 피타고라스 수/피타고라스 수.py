# https://www.acmicpc.net/problem/14398
from math import sqrt, gcd


def get_graph() -> list[list[int]]:
    graph = [[] for _ in range(n)]
    for i in range(n):
        ti = trees[i]
        for j in range(i+1, n):
            tj = trees[j]
            if gcd(ti, tj) == 1 and sqrt(ti*ti+tj*tj).is_integer():
                graph[i].append(j)
                graph[j].append(i)

    return graph


def dfs(one):
    if visited[one]:
        return False
    visited[one] = True

    for two in graph[one]:
        if matched[two] == -1:
            matched[two] = one
            return True
    for two in graph[one]:
        if dfs(matched[two]):
            matched[two] = one
            return True

    return False


n = int(input())
trees = list(map(int, input().split()))

graph: list[list[int]] = get_graph()

matched = [-1] * n
for one in range(n):
    visited = [False] * n
    dfs(one)

print((n - matched.count(-1)) >> 1)