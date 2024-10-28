# https://www.acmicpc.net/problem/17455
import sys
input = sys.stdin.readline
orders = ('K', 'D'), ('D', 'H'), ('H', 'K')


def topological_sort():
    stack, lengths = [], [-1] * (n+1)
    for idx, cnt in enumerate(counts[1:], 1):
        if not cnt:
            stack.append(idx)
            lengths[idx] = 1

    while stack:
        now = stack.pop()

        for nxt in graph[now]:
            counts[nxt] -= 1
            lengths[nxt] = max(lengths[nxt], lengths[now]+1)
            if not counts[nxt]:
                stack.append(nxt)

    # cycle 존재 확인
    if any(rest for rest in counts):
        return -1

    # H 에서 끝나는 값만이 길이로 인정
    ans = max((length//3*3 for idx, length in enumerate(lengths) if string[idx] == 'H'), default=0)
    return ans if ans else -1


n, m = map(int, input().split())
string = ' ' + input().rstrip()
graph, counts = [[] for _ in range(n+1)], [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    su, sv = string[u], string[v]
    if (su, sv) in orders:
        graph[u].append(v)
        counts[v] += 1
    elif (sv, su) in orders:
        graph[v].append(u)
        counts[u] += 1

print(topological_sort())