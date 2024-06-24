# https://www.acmicpc.net/problem/21606
import sys
input = sys.stdin.readline


def black(now):
    return sum(map(lambda near: 1 if a[near] == '1' else 0, graph[now]))


def white(now):
    visited[now] = 1
    st = [now]

    cnt = 0
    while st:
        x = st.pop()
        for nx in graph[x]:
            if visited[nx]:
                continue
            visited[nx] = 1

            if a[nx] == '0':
                st.append(nx)
            else:
                cnt += 1

    return cnt * (cnt-1)


n = int(input())
a = ' ' + input().rstrip()
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

total, visited = 0, [0] * (n+1)
for i in range(1, n+1):
    if a[i] == '1':
        total += black(i)
    elif not visited[i]:
        total += white(i)

print(total)