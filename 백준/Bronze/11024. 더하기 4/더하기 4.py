import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    ans.append(sum(map(int, input().split())))
print('\n'.join(map(str, ans)))