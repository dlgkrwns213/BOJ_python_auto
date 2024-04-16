# https://www.acmicpc.net/problem/27231
import sys
input = sys.stdin.readline


def sum_kth_powers(k):
    return sum(map(lambda num: num ** k, nums))


def backtracking(idx, location):
    global possible
    if idx == n-1:
        make_num, tmp = 0, 0
        for i in range(n):
            tmp *= 10
            tmp += nums[i]
            if location & (1 << i):
                make_num += tmp
                tmp = 0
        make_num += tmp

        if make_num in powers:
            possible.add(make_num)
        return

    backtracking(idx+1, location)
    backtracking(idx+1, location | (1 << idx))


ans = []
for _ in range(int(input())):
    nums = list(map(int, input().rstrip()))
    only_zeros_and_ones = all(num == 0 or num == 1 for num in nums)
    if only_zeros_and_ones:
        ans.append('Hello, BOJ 2023!')
        continue

    powers = set(sum_kth_powers(i) for i in range(1, 11))
    n = len(nums)
    possible = set()
    backtracking(0, 0)

    ans.append(len(possible))

print('\n'.join(map(str, ans)))