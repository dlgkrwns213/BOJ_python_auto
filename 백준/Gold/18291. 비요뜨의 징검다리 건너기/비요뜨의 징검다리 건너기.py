# https://www.acmicpc.net/problem/18291
import sys
input = sys.stdin.readline
MOD = int(1e9) + 7

ans = []
for _ in range(int(input())):
    n = max(2, int(input()))
    ans.append(pow(2, n-2, MOD))

print('\n'.join(map(str, ans)))