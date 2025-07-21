nums = sum([[x]*x for x in range(1, 46)], [])
a, b = map(int, input().split())
print(sum(nums[a-1:b]))