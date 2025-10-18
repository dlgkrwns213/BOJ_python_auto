import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    ans.append((a+b)**2 + c**2)

print('\n'.join(map(str, ans)))