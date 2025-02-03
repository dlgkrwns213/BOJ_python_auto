from itertools import accumulate

nums = list(map(int, input()))
prefix = [0] + list(accumulate(nums))

n, mx = len(nums), 0
for i in range(n):
    for j in range(i+2, n+1, 2):
        mid = i + j >> 1
        if prefix[j] + prefix[i] == 2 * prefix[mid]:
            mx = max(mx, j-i)

print(mx)