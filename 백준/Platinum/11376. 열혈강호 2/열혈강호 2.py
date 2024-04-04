# https://www.acmicpc.net/problem/11375
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


n, m = map(int, input().split())
works: list[tuple] = []
for _ in range(n):
    works.append(tuple(map(int, input().split()[1:])))

matched = [-1] * (m+1)
for person in range(n):
    for _ in range(2):
        visited = [False] * n
        dfs(person)

print(m+1 - matched.count(-1))