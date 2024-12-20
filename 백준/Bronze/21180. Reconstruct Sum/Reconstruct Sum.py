nums = [int(input()) for _ in range(int(input()))]

total = sum(nums)
print('BAD' if total % 2 or total // 2 not in nums else total // 2)