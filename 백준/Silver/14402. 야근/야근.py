import sys
from collections import defaultdict
input = sys.stdin.readline

rooms = defaultdict(int)
count = 0
for _ in range(int(input())):
    name, pm = input().split()

    if pm == "+":
        rooms[name] += 1
    else:
        if rooms[name]:
            rooms[name] -= 1
        else:
            count += 1

count += sum(rooms.values())
print(count)