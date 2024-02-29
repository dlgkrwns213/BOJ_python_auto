# https://www.acmicpc.net/problem/16438
from math import log2, ceil


def making(left, right, t):
    if right - left <= m:
        if t:
            for idx in range(left, right):
                team[idx] = 1
        return

    mid = left + right >> 1
    making(left, mid, t)
    making(mid, right, t ^ 1)


n = int(input())

teams, m = [], 1 << (ceil(log2(n))-1)
while m:
    team = [0] * n
    making(0, n, 0)

    m >>= 1

    team = ''.join(map(lambda t: 'A' if t else 'B', team))
    teams.append(team)

for _ in range(len(teams), 7):
    teams.append('B'*(n-1) + 'A')

print('\n'.join(teams))

'''
graph = {i: set(range(n)) for i in range(n)}
print(graph)
for team in teams:
    print(team)
    A = [i for i in range(n) if team[i] == 'A']
    B = [i for i in range(n) if team[i] == 'B']

    for a in A:
        for b in B:

            graph[a].discard(b)
            graph[b].discard(a)

for i in range(n):
    if graph[i] == {i}:
        del graph[i]
print(graph)  # {} 면 성공
'''