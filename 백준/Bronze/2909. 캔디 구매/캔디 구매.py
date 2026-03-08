c, k = map(int, input().split())

u = 10 ** k
print(((c + u//2) // u) * u)