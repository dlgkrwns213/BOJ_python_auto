# https://www.acmicpc.net/problem/14003
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

longest_parts, part_idx = [], []
for x in a:
    if not longest_parts or x > longest_parts[-1]:
        longest_parts.append(x)
        part_idx.append((len(longest_parts)-1, x))
    else:
        idx = bisect_left(longest_parts, x)
        longest_parts[idx] = x
        part_idx.append((idx, x))

ans, length = [], len(longest_parts)
last_idx = length - 1
for idx, val in part_idx[::-1]:
    if idx == last_idx:
        ans.append(val)
        last_idx -= 1

print(len(longest_parts))
print(' '.join(map(str, ans[::-1])))