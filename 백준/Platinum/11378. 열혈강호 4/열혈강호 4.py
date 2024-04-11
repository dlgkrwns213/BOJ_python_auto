# https://www.acmicpc.net/problem/11378
import sys
input = sys.stdin.readline


def dfs(person):
    if visited[person]:
        return False
    visited[person] = True

    for work in works[person]:
        if matched[work] == -1:
            matched[work] = person
            return True
    for work in works[person]:
        if dfs(matched[work]):
            matched[work] = person
            return True
    return False


n, m, k = map(int, input().split())
works = [list(map(lambda w: int(w)-1, input().split()[1:])) for _ in range(n)]

matched = [-1] * m
for p in range(n):
    visited = [False] * n
    dfs(p)

cnt = 0
for p in range(n):
    while cnt < k:
        visited = [False] * n
        if not dfs(p):
            break
        cnt += 1

    if cnt == k:
        break

print(m - matched.count(-1))