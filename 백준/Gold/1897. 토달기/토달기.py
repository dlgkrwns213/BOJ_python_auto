# https://www.acmicpc.net/problem/1897
import sys
from collections import deque
input = sys.stdin.readline


def is_conclude(word, find):
    if len(word) != len(find) + 1:
        return False

    return any(word[:idx] + word[idx+1:] == find for idx in range(len(word)))


def bfs():
    q = deque()
    q.append(0)

    visited = [0] * (d+1)
    visited[0] = 1

    now = 0
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append(nxt)

    return now


d, start = input().split()
d = int(d)

words = [start] + [input().rstrip() for _ in range(d)]

graph = [[] for _ in range(d+1)]
for i, iw in enumerate(words):
    for j, jw in enumerate(words[:i]):
        if is_conclude(iw, jw):
            graph[j].append(i)
        elif is_conclude(jw, iw):
            graph[i].append(j)

print(words[bfs()])