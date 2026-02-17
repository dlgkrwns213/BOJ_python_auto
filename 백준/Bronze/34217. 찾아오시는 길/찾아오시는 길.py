a, b = map(int, input().split())
c, d = map(int, input().split())

x = a + c
y = b + d

print(("Either", "Hanyang Univ.", "Yongdap")[(x < y) - (y < x)])