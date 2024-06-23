# https://www.acmicpc.net/problem/2262
n = int(input())
ranks = [-1] + list(map(int, input().split())) + [-1]

total = 0
for _ in range(n-1):
    idx = ranks.index(max(ranks))
    num = ranks[idx]
    total += num - max(ranks[idx+1], ranks[idx-1])
    ranks.remove(num)
print(total)