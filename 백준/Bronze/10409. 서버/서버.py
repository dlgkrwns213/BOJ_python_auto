_, t = map(int, input().split())
cnt, total = 0, 0
for work in map(int, input().split()):
    total += work
    if total > t:
        break
    cnt += 1
print(cnt)