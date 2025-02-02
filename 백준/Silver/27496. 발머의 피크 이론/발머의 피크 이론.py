n, l = map(int, input().split())
alcohols = list(map(int, input().split()))

cnt, now = 0, 0
for alcohol in alcohols[:l]:
    now += alcohol
    if 129 <= now <= 138:
        cnt += 1

for i in range(l, n):
    now += alcohols[i] - alcohols[i-l]
    if 129 <= now <= 138:
        cnt += 1

print(cnt)