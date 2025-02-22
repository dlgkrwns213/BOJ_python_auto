# https://www.acmicpc.net/problem/12972
from collections import Counter
from math import gcd


def get_max():
    global mx

    if counter[mx] > 1:
        counter[mx] -= 1
        return mx

    ret = mx
    del counter[mx]
    mx = max(counter)  # 새로운 mx
    return ret


def find_nums():
    global mx
    if n == 1:
        return gcds

    nums = [get_max()]
    for _ in range(n-1):
        new = get_max()
        for num in nums:
            g = gcd(new, num)
            counter[g] -= 2
            if not counter[g]:
                del counter[g]
                if mx == g:
                    mx = max(counter, default=0)
        nums.append(new)

    return nums


n = int(input())
gcds = list(map(int, input().split()))

mx = max(gcds)
counter = Counter(gcds)

print(' '.join(map(str, find_nums())))