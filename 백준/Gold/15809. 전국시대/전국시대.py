# https://www.acmicpc.net/problem/15809
import sys
input = sys.stdin.readline


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(uw, a, b):
    x = find(a)
    y = find(b)

    if troops[x] > troops[y]:
        parent[y] = x
        troops[x] += troops[y] * (1 if uw==1 else -1)
        troops[y] = 0
    else:
        parent[x] = y
        troops[y] += troops[x] * (1 if uw==1 else -1)
        troops[x] = 0
        

n, m = map(int, input().split())
troops = [0] + [int(input()) for _ in range(n)]

parent = list(range(n+1))
for _ in range(m):
    union(*map(int, input().split()))

rest = sorted(troop for troop in troops if troop)
print(len(rest))
print(' '.join(map(str, rest)))