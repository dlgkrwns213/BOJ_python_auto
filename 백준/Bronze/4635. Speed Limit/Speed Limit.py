ans = []

while True:
    n = int(input())
    if n == -1:
        break

    pt = 0
    d = 0

    for _ in range(n):
        s, t = map(int, input().split())
        d += s * (t - pt)
        pt = t

    ans.append(d)

print("\n".join(map(lambda x: f"{x} miles", ans)))