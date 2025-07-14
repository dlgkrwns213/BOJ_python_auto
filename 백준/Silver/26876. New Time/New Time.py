sh, sm = map(int, input().split(":"))
dh, dm = map(int, input().split(":"))

cnt = dm - sm
if sm > dm:
    cnt += 60
    sh += 1

cnt += (dh - sh) % 24
print(cnt)