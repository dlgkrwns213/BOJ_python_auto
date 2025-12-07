import sys
input = sys.stdin.readline

print(sorted([x for x in (input() for _ in range(int(input()))) if len(x) == 4])[0][:-1])