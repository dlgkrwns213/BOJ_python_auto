import sys
from collections import defaultdict
input = sys.stdin.readline

counts = defaultdict()
total = 0
xor = 0

answer = []
for _ in range(int(input())):
    command, *number = map(int, input().split())
    if command == 1:
        [number] = number
        total += number
        xor ^= number
    elif command == 2:
        [number] = number
        total -= number
        xor ^= number
    elif command == 3:
        answer.append(total)
    elif command == 4:
        answer.append(xor)

print('\n'.join(map(str, answer)))