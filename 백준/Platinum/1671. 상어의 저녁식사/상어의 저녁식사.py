# https://www.acmicpc.net/problem/1671
import sys
input = sys.stdin.readline


def dfs(now):
    if visited[now]:
        return False
    visited[now] = True

    for food in graph[now]:
        if matched[food] == -1:
            matched[food] = now
            return True
    for food in graph[now]:
        if dfs(matched[food]):
            matched[food] = now
            return True
    return False


# 완전히 동일하다면 한마리로 취급해도
n = int(input())
sharks = list(tuple(map(int, input().split())) for _ in range(n))

graph = [[] for _ in range(n)]
for ia, va in enumerate(sharks):
    for ib, vb in enumerate(sharks):
        if ia == ib:
            continue

        if va == vb:  # 동일한 스펙의 상어일 때
            if ia < ib:  # 먼저 나온 상어가 먹기
                graph[ia].append(ib)
        elif all(va[i] >= vb[i] for i in range(3)):
            graph[ia].append(ib)

matched = [-1] * n
for shark in range(n):
    for _ in range(2):
        visited = [False] * n
        dfs(shark)

print(matched.count(-1))