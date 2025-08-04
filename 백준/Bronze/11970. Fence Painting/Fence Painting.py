a, b = map(int, input().split())
c, d = map(int, input().split())

x = [0] * 101
for i in range(a, b):
    x[i] = 1
for i in range(c, d):
    x[i] = 1

print(sum(x))