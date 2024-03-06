# https://www.acmicpc.net/problem/2150
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(now):
    global order
    visited[now] = order  # 내가 몇번쨰로 탐색되었는가
    order += 1

    stack.append(now)
    group_first = visited[now]  # 그룹에서 첫번째로 탐색된 노드가 몇번째로 탐색되었는지 저장
    for nxt in graph[now]:
        # 내가 갈수 있는 노드 중에서 앞서 진입한 노드가 존재하는지 확인
        nxt_group_first = visited[nxt] if visited[nxt] else dfs(nxt)
        group_first = min(group_first, nxt_group_first)

    # 내가 현재 그룹에서 가장 첫번째로 탐색되었으면 -> 나보다 나중에 탐색된 노드들은 모두 나와 같은 그룹
    if group_first == visited[now]:
        group = []
        while 1:
            top = stack.pop()
            visited[top] = v+1  # 다른 시작점에서 들어온 경우 무조건 현재보다 작은 수로 인식되기 때문에 최대로 설정
            group.append(top)
            if top == now:
                break

        ans.append(sorted(group))
    return group_first


v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

visited, order, stack = [0] * (v+1), 1, []
ans = []
for start in range(1, v+1):
    if not visited[start]:
        dfs(start)

ans.sort(key=lambda line: line[0])
print(len(ans))
for line in ans:
    line.append(-1)
    print(' '.join(map(str, line)))