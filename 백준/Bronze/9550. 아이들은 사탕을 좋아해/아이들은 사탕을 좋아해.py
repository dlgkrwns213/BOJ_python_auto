import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    ans.append(sum(map(lambda x: int(x)//k, input().split())))

print('\n'.join(map(str, ans)))