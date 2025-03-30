# https://www.acmicpc.net/problem/28017
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
now = [0] * m
for _ in range(n):
    times = list(map(int, input().split()))
    nxt = list(map(lambda i: times[i] + min([now[j] for j in range(m) if i != j]), range(m)))
    now = nxt

print(min(now))
