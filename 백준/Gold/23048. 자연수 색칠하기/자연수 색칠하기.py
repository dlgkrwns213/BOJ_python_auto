n = int(input())

colors = [0] * (n+1)
colors[1] = 1

color = 1
for i in range(2, n+1):
    if not colors[i]:
        color += 1
        for j in range(i, n+1, i):
            colors[j] = color

print(color)
print(' '.join(map(str, colors[1:])))