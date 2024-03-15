# https://www.acmicpc.net/problem/23559
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
B, gaps = [0] * n, [0] * n
for i in range(n):
    a, b = map(int, input().split())
    gaps[i] = a-b if a > b else 0
    B[i] = b
    
gaps.sort(reverse=True)
a_time = (x-1000*n) // 4000  # A에서 가서 밥을 먹을수 있는 최대 횟수

print(sum(B) + sum(gaps[:a_time]))