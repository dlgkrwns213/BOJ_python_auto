# https://www.acmicpc.net/problem/3078
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lengths = [len(input().rstrip()) for _ in range(n)]

cnt, total = [0] * 21, 0
for i, length in enumerate(lengths):
    total += cnt[length]

    if i >= k:
        cnt[lengths[i-k]] -= 1
        
    cnt[length] += 1

print(total)