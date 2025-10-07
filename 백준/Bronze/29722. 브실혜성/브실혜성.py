y, m, d = map(int, input().split('-'))
n = int(input())

total = y * 360 + (m-1) * 30 + (d-1) + n

ny, total = divmod(total, 360)
nm, nd = divmod(total, 30)

print(f"{ny:04d}-{nm+1:02d}-{nd+1:02d}")