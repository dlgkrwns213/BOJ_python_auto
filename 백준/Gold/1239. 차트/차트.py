from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))

mx = 0
for now in permutations(nums, n):
    prefix = [0] * (n+1)
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + now[i-1]

    spre = set(prefix)
    mx = max(mx, sum(map(lambda x: 1 if x+50 in spre else 0, prefix)))

print(max(mx-1, 0))