import sys
input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    answer.append((a//b) ** 2)

print('\n'.join(map(str, answer)))