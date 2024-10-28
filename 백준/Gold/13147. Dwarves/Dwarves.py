# https://www.acmicpc.net/problem/13147
import sys
input = sys.stdin.readline


def topological_sort() -> bool:
    stack = []
    for idx, cnt in enumerate(counts):
        if not cnt:
            stack.append(idx)

    while stack:
        now = stack.pop()

        for nxt in graph[now]:
            counts[nxt] -= 1
            if not counts[nxt]:
                stack.append(nxt)

    return any(rest for rest in counts)


n = int(input())
indexs = {}
graph, counts = [[] for _ in range(2*n)], [0] * (2*n)
for _ in range(n):
    s1, sign, s2 = input().split()

    i1 = indexs.setdefault(s1, len(indexs))
    i2 = indexs.setdefault(s2, len(indexs))

    if sign == '>':
        graph[i1].append(i2)
        counts[i2] += 1
    else:
        graph[i2].append(i1)
        counts[i1] += 1

print(f'{"im" if topological_sort() else ""}possible')