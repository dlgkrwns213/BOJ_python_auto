from math import factorial

w, l, d = map(float, input().split())

percents = [0] * 5
for i in range(21):
    for j in range(21-i):
        weight = factorial(20) // factorial(i) // factorial(j) // factorial(20-i-j)

        score = 1000 + i * 50 - j * 50
        percents[score//500] += w ** i * l ** j * d ** (20-i-j) * weight

print('\n'.join(map(lambda percent: f'{percent:.8f}', percents)))