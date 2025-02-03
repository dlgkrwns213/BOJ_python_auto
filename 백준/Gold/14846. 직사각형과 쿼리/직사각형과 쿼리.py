# https://www.acmicpc.net/problem/14846
import sys
input = sys.stdin.readline


def plus(a: list, b: list) -> list:
    return [x + y for x, y in zip(a, b)]


def minus(a: list, b: list) -> list:
    return [x - y for x, y in zip(a, b)]


n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

prefix = [[[0]*10 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        prefix[i+1][j+1] = minus(plus(prefix[i+1][j], prefix[i][j+1]), prefix[i][j])
        prefix[i+1][j+1][nums[i][j]-1] += 1

ans = []
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    total = minus(plus(prefix[x2][y2], prefix[x1-1][y1-1]), plus(prefix[x2][y1-1], prefix[x1-1][y2]))
    ans.append(10 - total.count(0))
print('\n'.join(map(str, ans)))