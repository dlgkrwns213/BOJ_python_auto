zz, zo = 1, 0  # 0부터 시작
oz, oo = 0, 1  # 1부터 시작

for time in range(1, int(input())):
    zz, zo, oz, oo = zz + oz, zo + oo, zz + oz, zo + oo
    if not time & 1:
        zo -= 1
        oz -= 1

print(oz)