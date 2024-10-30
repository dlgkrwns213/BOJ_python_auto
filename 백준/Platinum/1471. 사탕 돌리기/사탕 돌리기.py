# https://www.acmicpc.net/problem/1471
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
sum_of_digits = lambda number: (number // 100000) + ((number // 10000) % 10) + ((number // 1000) % 10) + \
                ((number // 100) % 10) + ((number // 10) % 10) + (number % 10)


def dfs(now):
    global order
    visited[now] = order
    order += 1
    stack.append(now)

    nxt = nexts[now]
    group_first = min(visited[now], visited[nxt] if visited[nxt] else dfs(nxt))

    if group_first == visited[now]:
        cnt = 0
        while stack:
            top = stack.pop()
            visited[top] = n+1
            my_represent[top] = now
            cnt += 1

            if top == now:
                break
        represent_counts[now] = cnt
    return group_first


def dfs_rep(now_rep):
    ret = 0
    for nxt_rep in represent_graph[now_rep]:
        if visited_rep[nxt_rep]:
            continue
        visited_rep[nxt_rep] = 1
        ret = max(ret, dfs_rep(nxt_rep))

    return ret + represent_counts[now_rep]


n = int(input())
nexts = list(range(n+1))

for num in range(1, n+1):
    digit = sum_of_digits(num)
    nexts[num] = (num + digit - 1) % n + 1

visited, order = [0] * (n+1), 1
stack, represent_counts, my_represent = [], dict(), list(range(n+1))
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

represents = {rep for rep in represent_counts}
represent_graph = {rep: [] for rep in represent_counts}
for rep in represents:
    nxt_rep = my_represent[nexts[rep]]
    if rep != nxt_rep:
        represent_graph[nxt_rep].append(rep)

visited_rep, mx = {rep: 0 for rep in represents}, 0
for rep in represents:
    if represent_counts[rep] != 1 or nexts[rep] == rep:
        mx = max(mx, dfs_rep(rep))
print(mx)