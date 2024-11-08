import sys
input = sys.stdin.readline

win = [0, 0]
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        continue
    win[a<b] += 1

print(*win)