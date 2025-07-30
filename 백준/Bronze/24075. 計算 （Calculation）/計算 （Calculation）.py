a, b = map(int, input().split())
x, y = a+b, a-b
print(f'{max(x, y)}\n{min(x, y)}')