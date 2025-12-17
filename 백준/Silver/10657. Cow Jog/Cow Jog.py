import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    _, p = map(int, input().split())
    while stack and stack[-1] > p:
        stack.pop()

    stack.append(p)

print(len(stack))