n = int(input())
m = int(input())

count = 0
for i in range(n*m):
    ix, iy = divmod(i, m)
    for j in range(i):
        jx, jy = divmod(j, m)

        if iy-jy == 1 and abs(ix-jx) == 1:
            count += 1

print(2*count)