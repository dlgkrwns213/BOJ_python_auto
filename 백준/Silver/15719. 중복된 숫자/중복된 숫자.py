import sys

n = int(input())

total = 0
tmp = []
for char in sys.stdin.read():
    if char == ' ':
        total += int(''.join(tmp))
        tmp = []
    else:
        tmp.append(char)

total += int(''.join(tmp))
print(total - n * (n-1) // 2)