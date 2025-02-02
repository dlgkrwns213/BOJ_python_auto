# https://www.acmicpc.net/problem/21757
from itertools import accumulate
from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))

prefix = [0] + list(accumulate(nums))
if prefix[n] % 4:
    print(0)
else:
    one = prefix[n] >> 2
    if one:
        counts = [[] for _ in range(3)]

        for i, p in enumerate(prefix):
            if not p % one and 0 < p // one < 4:
                counts[p//one-1].append(i)

        three, total = len(counts[2]), 0
        for i in counts[0]:
            for j in counts[1][bisect_left(counts[1], i+1):]:
                total += three - bisect_left(counts[2], j+1)

        print(total)
    else:
        count = prefix.count(0) - 2
        print((count-2)*(count-1)*count//6)
