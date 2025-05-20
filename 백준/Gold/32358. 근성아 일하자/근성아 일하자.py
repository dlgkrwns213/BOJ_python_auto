# https://www.acmicpc.net/problem/32358
import sys
input = sys.stdin.readline
INF = int(1e9)

wastes = {-INF, INF}
now, total = 0, 0
for _ in range(int(input())):
    q, *x = map(int, input().split())
    if q == 1:
        wastes.add(x[0])
        continue

    sorted_wastes = sorted(wastes)
    left, right = 0, 0
    for i in range(len(sorted_wastes)-1):
        if sorted_wastes[i] <= now <= sorted_wastes[i+1]:
            left, right = i, i+1
            break

    for _ in range(len(sorted_wastes)-2):
        if now - sorted_wastes[left] <= sorted_wastes[right] - now:
            total += now - sorted_wastes[left]
            now = sorted_wastes[left]
            left -= 1
        else:
            total += sorted_wastes[right] - now
            now = sorted_wastes[right]
            right += 1

    wastes = {-INF, INF}

print(total)