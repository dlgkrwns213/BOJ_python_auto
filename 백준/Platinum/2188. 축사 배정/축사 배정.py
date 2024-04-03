# https://www.acmicpc.net/problem/2188
import sys
input = sys.stdin.readline


def dfs(cow):
    if visited[cow]:
        return False
    visited[cow] = True

    for house in houses[cow]:
        if matched[house] == -1 or dfs(matched[house]):
            matched[house] = cow
            return True

    return False


n, m = map(int, input().split())
houses: list[tuple] = []
for _ in range(n):
    houses.append(tuple(map(int, input().split()[1:])))

matched = [-1] * (m+1)
for cow in range(n):
    visited = [0] * n
    dfs(cow)

print(m+1 - matched.count(-1))