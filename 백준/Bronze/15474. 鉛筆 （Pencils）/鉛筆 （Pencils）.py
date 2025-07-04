from math import ceil

N, A, B, C, D = map(int, input().split())

cost_X = ceil(N / A) * B
cost_Y = ceil(N / C) * D

print(min(cost_X, cost_Y))