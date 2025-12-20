import sys
input = sys.stdin.readline

n, b = map(int, input().split())
heights = sorted([int(input()) for _ in range(n)], reverse=True)

total, count = 0, 0
for height in heights:
    total += height
    count += 1

    if total >= b:
        break

print(count)