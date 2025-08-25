n = int(input())

total, now = 0, 0
for x in input().split():
    if x == '1':
        now += 1
    else:
        now -= 1

    total += now

print(total)