a, b = map(int, input().split())

x = int((a*a-b)**.5)
print(*(-a-x, -a+x) if x else (-a,))