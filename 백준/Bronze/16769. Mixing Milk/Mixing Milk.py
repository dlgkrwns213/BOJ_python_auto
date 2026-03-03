c = []
m = []

for _ in range(3):
    x, y = map(int, input().split())
    c.append(x)
    m.append(y)

for i in range(100):
    f = i % 3
    t = (i+1) % 3
    p = min(m[f], c[t] - m[t])
    m[f] -= p
    m[t] += p

print('\n'.join(map(str, m)))