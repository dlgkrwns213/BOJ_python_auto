bef, cnt = '', 0
total = 1
change = {'d': 10, 'c': 26}
for x in input():
    if bef != x:
        if cnt:
            total *= (10 * (9 ** (cnt-1))) if bef == 'd' else (26 * (25 ** (cnt-1)))
        bef, cnt = x, 1
    else:
        cnt += 1

total *= (10 * (9 ** (cnt-1))) if bef == 'd' else (26 * (25 ** (cnt-1)))
print(total)