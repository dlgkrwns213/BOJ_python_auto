import sys
input = sys.stdin.readline

print(sum(sum(map(int, input().split())) for _ in range(int(input()))))