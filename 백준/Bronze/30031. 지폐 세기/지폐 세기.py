costs = {136: 1000, 142: 5000, 148: 10000, 154: 50000}

total = 0
for _ in range(int(input())):
    sizes = list(map(int, input().split()))
    for size in costs:
        if size in sizes:
            total += costs[size]
            break

print(total)