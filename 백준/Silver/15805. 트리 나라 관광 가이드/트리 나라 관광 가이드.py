n = int(input()) + 1 >> 1

parents, visited, parent = [-1] * n, [False] * n, -1
for node in map(int, input().split()):
    if not visited[node]:
        visited[node] = True
        parents[node] = parent

    parent = node

print(n)
print(' '.join(map(str, parents)))