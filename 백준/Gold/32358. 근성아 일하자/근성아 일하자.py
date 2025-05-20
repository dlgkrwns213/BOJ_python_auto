# https://www.acmicpc.net/problem/32358
import sys
input = sys.stdin.readline
INF = int(1e9)

wastes = [-INF, INF]
now, total = 0, 0
for _ in range(int(input())):
    q, *x = map(int, input().split())
    if q == 1:
        wastes.append(x[0])
        continue

    wastes.sort()
    left, right = 0, 0
    for i in range(len(wastes)-1):
        if wastes[i] <= now <= wastes[i+1]:
            left, right = i, i+1

    for _ in range(len(wastes)-2):
        if now - wastes[left] <= wastes[right] - now:
            total += now - wastes[left]
            now = wastes[left]
            left -= 1
        else:
            total += wastes[right] - now
            now = wastes[right]
            right += 1

    wastes = [-INF, INF]

print(total)