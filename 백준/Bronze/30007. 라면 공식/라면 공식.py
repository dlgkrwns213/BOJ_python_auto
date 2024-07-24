import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    a, b, x = map(int, input().split())
    ans.append(a*(x-1)+b)

print('\n'.join(map(str, ans)))