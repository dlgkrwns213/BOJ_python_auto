# https://www.acmicpc.net/problem/3780
import sys
input = sys.stdin.readline


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(main, sub):
    x = find(main)
    y = find(sub)

    connect[sub] = main
    distance[sub] = abs(main-sub) % 1000

    parent[x] = y


ans = []
for _ in range(int(input())):
    n = int(input())
    parent = list(range(n+1))
    connect, distance = list(range(n+1)), [0] * (n+1)
    while True:
        q, *tmp = input().split()
        if q == 'E':
            i = int(*tmp)
            now = 0
            while i != connect[i]:
                now += distance[i]
                i = connect[i]
            ans.append(now)
        elif q == 'I':
            i, j = map(int, tmp)
            union(j, i)
        else:
            break

print('\n'.join(map(str, ans)))