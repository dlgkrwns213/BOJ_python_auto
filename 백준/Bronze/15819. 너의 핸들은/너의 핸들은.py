import sys
input = sys.stdin.readline

n, i = map(int, input().split())
words = sorted(input().rstrip() for _ in range(n))

print(words[i-1])