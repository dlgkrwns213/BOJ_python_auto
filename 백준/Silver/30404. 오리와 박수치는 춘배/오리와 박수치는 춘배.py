n, k = map(int, input().split())

now, count = -k, 0
for x in map(int, input().split()):
    if now + k >= x:
        continue

    now = x
    count += 1

print(count)