bef, cnt = '', 0
total = 1
for x in input():
    if bef != x:
        if cnt:
            if bef == 'd':
                total *= 10 * (9 ** (cnt-1))
            else:
                total *= 26 * (25 ** (cnt-1))

        bef, cnt = x, 1
    else:
        cnt += 1

total *= (10 * (9 ** (cnt-1))) if bef == 'd' else (26 * (25 ** (cnt-1)))
print(total)