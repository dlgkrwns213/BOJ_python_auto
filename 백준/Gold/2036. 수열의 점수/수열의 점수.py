# https://www.acmicpc.net/problem/2036
import sys
input = sys.stdin.readline


def get_max(nums):
    ret = 0
    while nums:
        ret += nums.pop() * (nums.pop() if nums else 1)
    return ret


n = int(input())
nums = [int(input()) for _ in range(n)]

down_one, up_one = sorted((num for num in nums if num < 1), reverse=True), sorted(num for num in nums if num > 1)
print(len(nums)-len(down_one)-len(up_one)+get_max(down_one)+get_max(up_one))