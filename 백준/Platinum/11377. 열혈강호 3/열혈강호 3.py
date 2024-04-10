# https://www.acmicpc.net/problem/11377
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
works, people = [[] for _ in range(n)], [[] for _ in range(m)]
for p in range(n):
    for w in map(lambda x: int(x)-1, input().split()[1:]):
        works[p].append(w)
        people[w].append(p)

matched = [-1] * m
for p in range(n):
    visited = [False] * n
    dfs(p)
one = m - matched.count(-1)

two = 0
for p in range(n):
    visited = [False] * n
    if dfs(p):
        two += 1
        if two == k:
            break

print(one + two)