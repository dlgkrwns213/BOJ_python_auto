n = int(input())
nums = list(map(int, input().split()))

total, rest = 0, sum(nums)
for num in nums:
    rest -= num
    total += num * rest

print(total)