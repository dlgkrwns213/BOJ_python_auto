import sys
input = sys.stdin.readline


def backtracking(idx, cnt, up):
    global mx
    mx = max(mx, cnt)
    if idx == n+1:
        return
    backtracking(idx+1, cnt, up)

    if up & 1 << idx:
        return
    up |= 1 << idx
    for friend in graph[idx]:
        if not up & (1 << friend):
            backtracking(idx+1, cnt+2, up | 1 << friend)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    graph[u].append(v)

mx = 0
backtracking(1, 0, 0)
if mx < n:
    mx += 1
print(mx)