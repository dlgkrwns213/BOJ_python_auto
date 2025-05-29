answer = 1

def solution(info, edges):
    visited = [0] * len(info)
    visited[0] = 1
    dfs(info, edges, visited, 1, 0)
    return answer


def dfs(info, edges, visited, sheep, wolf):
    global answer
    if sheep == wolf:
        return
    answer = max(answer, sheep)
    
    for parent, child in edges:
        if visited[parent] and not visited[child]:
            visited[child] = 1
            if not info[child]:
                dfs(info, edges, visited, sheep+1, wolf)
            else:
                dfs(info, edges, visited, sheep, wolf+1)
            visited[child] = 0