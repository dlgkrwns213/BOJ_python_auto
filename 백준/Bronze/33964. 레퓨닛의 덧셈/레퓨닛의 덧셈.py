x, y = map(int, input().split())
if x > y:
    x, y = y, x

print('1'*(y-x) + '2'*x)