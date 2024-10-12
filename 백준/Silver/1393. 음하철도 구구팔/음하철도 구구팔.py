from math import sqrt, gcd
distance = lambda si, sj, ei, ej: sqrt((si - ei) ** 2 + (sj - ej) ** 2)

sx, sy = map(int, input().split())
ex, ey, dx, dy = map(int, input().split())

dg = gcd(dx, dy)
dx //= dg
dy //= dg

mn = distance(sx, sy, ex, ey)
while True:
    now = distance(sx, sy, ex + dx, ey + dy)
    if mn < now:
        break
    mn = now

    ex += dx
    ey += dy

print(ex, ey)