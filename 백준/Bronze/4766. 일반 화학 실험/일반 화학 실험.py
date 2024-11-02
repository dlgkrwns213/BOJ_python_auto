ans, bef = [], float(input())
while True:
    now = float(input())
    if now == 999.:
        break
    ans.append(f'{now-bef:.2f}')
    bef = now

print('\n'.join(map(str, ans)))