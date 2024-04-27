# https://www.acmicpc.net/problem/18869
import sys
from collections import Counter
input = sys.stdin.readline

m, n = map(int, input().split())
spaces: list[tuple[int]] = [None] * m
for i in range(m):
    space: list = list(map(int, input().split()))

    orders = sorted(set(space))
    planet2order: dict = {planet: order for order, planet in enumerate(orders)}
    space_order: tuple = tuple(map(lambda planet: planet2order[planet], space))

    spaces[i] = space_order

total = 0
for cnt in Counter(spaces).values():
    total += cnt * (cnt - 1) >> 1

print(total)