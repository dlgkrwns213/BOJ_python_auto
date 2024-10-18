a = int(input())
t = int(input())
want = int(input())

cnt, total = 4, 0
while cnt < t:
    t -= cnt
    total += cnt << 1
    cnt += 1

for idx, say in enumerate([0, 1, 0, 1] + [0] * (cnt-2) + [1] * (cnt-2)):
    if say == want:
        t -= 1
        if not t:
            total += idx
            break

print(total % a)