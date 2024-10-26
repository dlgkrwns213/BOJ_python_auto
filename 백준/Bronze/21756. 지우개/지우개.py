n = int(input())

x = list(range(1, n+1))
while len(x) > 1:
    x = [v for i, v in enumerate(x) if i % 2]

print(x[0])