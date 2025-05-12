# https://www.acmicpc.net/problem/28018
import sys
input = sys.stdin.readline

times = [0] * 1000002
for _ in range(int(input())):
    s, e = map(int, input().split())
    times[s] += 1
    times[e+1] -= 1

for i in range(1, 1000002):
    times[i] += times[i-1]

input()
print('\n'.join(map(lambda x: str(times[x]), map(int, input().split()))))