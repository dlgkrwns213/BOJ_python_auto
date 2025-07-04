N, A, B, C, D = map(int, input().split())

cost_X = (N+A-1) // A * B
cost_Y = (N+C-1) // C * D

print(min(cost_X, cost_Y))