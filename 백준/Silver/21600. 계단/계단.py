n = int(input())

mx, now = 0, 0
for num in map(int, input().split()):
    if num > now:
        now += 1
        mx = max(mx, now)
    else:
        now = num

print(mx)