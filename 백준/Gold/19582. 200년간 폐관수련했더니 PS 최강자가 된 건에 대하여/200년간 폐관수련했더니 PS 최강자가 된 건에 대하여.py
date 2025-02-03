# https://acmicpc.net/problem/19582
import sys
input = sys.stdin.readline
INF = float('inf')

bef_zero, bef_one = 0, 0
possible = True
for _ in range(int(input())):
    mn, add = map(int, input().split())
    zero = bef_zero + add if bef_zero <= mn else INF
    one = min(bef_zero, bef_one + add if bef_one <= mn else INF)
    if one == INF:
        possible = False

    bef_zero, bef_one = zero, one

print('Kkeo-eok' if possible else 'Zzz')