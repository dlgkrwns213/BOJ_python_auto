n = int(input())
xs = sorted(map(int, input().split()))

count = 0
now, mx = 0, 0
for x in xs:
    now += 1
    if now > mx:
        now = 1
        count += 1
        mx = x

print(count)