ans = []
while True:
    x, y = map(int, input().split())
    if not y:
        break
    a, b = divmod(x, y)
    ans.append(f'{a} {b} / {y}')

print('\n'.join(ans))