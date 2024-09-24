change = {'kg': (2.2046, 'lb'), 'lb': (0.4536, 'kg'), 'l': (0.2642, 'g'), 'g': (3.7854, 'l')}

ans = []
for _ in range(int(input())):
    x, d = input().split()
    y, nd = change[d]
    ans.append(f'{float(x)*y:.4f} {nd}')
print('\n'.join(ans))