# https://www.acmicpc.net/problem/16402
import sys
input = sys.stdin.readline


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(winner, loser):
    wr = find(winner)
    lr = find(loser)
    if wr == lr:
        real[wr] = winner
    else:
        parent[lr] = wr


n, m = map(int, input().split())
countries = [None] * n
for i in range(n):
    *_, c = input().split()
    countries[i] = c
country_idx = {c: i for i, c in enumerate(countries)}

parent, real = list(range(n)), list(range(n))
for _ in range(m):
    x, y, w = input().rstrip().split(',')
    *_, x = x.split()
    *_, y = y.split()
    if w == '1':
        union(country_idx[x], country_idx[y])
    else:
        union(country_idx[y], country_idx[x])

rest_countries = sorted(set(map(lambda idx: countries[real[find(idx)]], parent)))
print(len(rest_countries))
print('\n'.join(map(lambda country: f'Kingdom of {country}', rest_countries)))