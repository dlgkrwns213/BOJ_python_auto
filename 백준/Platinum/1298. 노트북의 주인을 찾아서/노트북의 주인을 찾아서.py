# https://www.acmicpc.net/problem/1298
import sys
input = sys.stdin.readline


def dfs(person: int):
    if visited[person]:
        return False
    visited[person] = True

    for computer in computers[person]:
        if matched[computer] == -1:
            matched[computer] = person
            return True
    for computer in computers[person]:
        if dfs(matched[computer]):
            matched[computer] = person
            return True
    return False


n, m = map(int, input().split())
computers = [[] for _ in range(n+1)]
for _ in range(m):
    person, computer = map(int, input().split())
    computers[person].append(computer)

matched = [-1] * (n+1)
for p in range(1, n+1):
    visited = [False] * (n+1)
    dfs(p)

print(n+1 - matched.count(-1))