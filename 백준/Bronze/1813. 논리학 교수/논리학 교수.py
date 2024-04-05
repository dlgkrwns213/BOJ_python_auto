n = int(input())
counts = [0] * 51
for x in map(int, input().split()):
    counts[x] += 1

ans = -1
for x in range(50, -1, -1):
    if counts[x] == x:
        ans = x
        break

print(ans)