import sys
from collections import deque
input = sys.stdin.readline

deq = deque()
for idx in range(int(input())):
    command, *alpha = input().split()
    if command == '1':
        [alpha] = alpha
        deq.append((alpha, idx))
        is_front = False
    elif command == '2':
        [alpha] = alpha
        deq.appendleft((alpha, idx))
        is_front = True
    elif deq:
        if deq[0][1] < deq[-1][1]:
            deq.pop()
        else:
            deq.popleft()

print(''.join(map(lambda block: block[0], deq)) if deq else 0)