import sys
input = sys.stdin.readline

n = int(input())
lines = []
events = []
for i in range(n):
    s, e = map(int, input().split())
    lines.append((s, e, i+1))
    events.append((s, 1))
    events.append((e, -1))
events.sort(key=lambda event: (event[0], -event[1]))

max_val = 0
now_val = 0
max_spot = 0

for event, pm in events:
    now_val += pm
    if max_val < now_val:
        max_val = now_val
        max_spot = event

answer = []
for s, e, idx in lines:
    if s <= max_spot <= e:
        answer.append(idx)

print(max_val)
print(' '.join(map(str, answer[:max_val])))