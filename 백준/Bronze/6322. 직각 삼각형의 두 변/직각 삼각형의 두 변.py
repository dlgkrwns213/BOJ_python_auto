from math import sqrt

for tc in range(1, int(1e6)):
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break

    print(f'Triangle #{tc}')
    if a == -1:
        x = c * c - b * b
        print(f'a = {sqrt(x):.3f}' if x > 0 else 'Impossible.')
    elif b == -1:
        x = c * c - a * a
        print(f'b = {sqrt(x):.3f}' if x > 0 else 'Impossible.')
    else:
        print(f'c = {sqrt(a*a + b*b):.3f}')
    print()