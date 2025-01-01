costs = [0, 500, 800, 1000]
print(5000 - sum(map(lambda i: costs[i], map(int, input().split()))))