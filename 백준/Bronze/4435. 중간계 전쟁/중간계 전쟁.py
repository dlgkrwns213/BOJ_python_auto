score_a = [1, 2, 3, 3, 4, 10]
score_b = [1, 2, 2, 2, 3, 5, 10]

for t in range(int(input())):
    count_a = list(map(int, input().split()))
    count_b = list(map(int, input().split()))

    a = sum(map(lambda idx: score_a[idx] * count_a[idx], range(6)))
    b = sum(map(lambda idx: score_b[idx] * count_b[idx], range(7)))

    if a == b:
        ans = 'No victor on this battle field'
    elif a > b:
        ans = 'Good triumphs over Evil'
    else:
        ans = 'Evil eradicates all trace of Good'

    print(f'Battle {t+1}: {ans}')