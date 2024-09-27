n = int(input())

now, cnt = 'E', 0
for x in input():
    if x != now:
        now = x
        cnt += 1

print(cnt+1>>1)