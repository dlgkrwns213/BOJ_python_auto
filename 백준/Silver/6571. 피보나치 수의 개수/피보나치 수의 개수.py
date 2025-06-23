fibo = [0] * 500
fibo[1] = 1
fibo[2] = 2
for i in range(3, 500):
    fibo[i] = fibo[i-1] + fibo[i-2]

    if fibo[i] >= int(1e100):
        break

ans = []
while True:
    a, b = map(int, input().split())
    if not a and not b:
        break

    count = 0
    for c in range(1, 500):
        if a <= fibo[c] <= b:
            count += 1
        elif b < fibo[c]:
            break

    ans.append(count)
print('\n'.join(map(str, ans)))