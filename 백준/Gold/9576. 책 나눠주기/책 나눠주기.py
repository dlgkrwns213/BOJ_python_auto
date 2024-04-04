import sys
input = sys.stdin.readline


def dfs(now):
    if visited[now]:
        return False
    visited[now] = True

    a, b = book_range[now]
    for book in range(a, b+1):
        if matched[book] == -1:
            matched[book] = now
            return True
    for book in range(a, b+1):
        if dfs(matched[book]):
            matched[book] = now
            return True
    return False


ans = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    book_range = [tuple(map(int, input().split())) for _ in range(m)]

    matched = [-1] * (n+1)
    for i in range(m):
        visited = [False] * m
        dfs(i)

    ans.append(n+1 - matched.count(-1))

print('\n'.join(map(str, ans)))
