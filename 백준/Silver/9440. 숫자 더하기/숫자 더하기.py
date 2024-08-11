import sys
input = sys.stdin.readline

ans = []
while True:
    n, *nums = map(int, input().split())
    if not n:
        break

    nums.sort()
    for i in range(n):
        if nums[i]:
            a, b = nums[i], nums[i+1]
            nums = nums[:i] + nums[i+2:]
            break

    for i, num in enumerate(nums):
        if i % 2:
            b = 10 * b + num
        else:
            a = 10 * a + num

    ans.append(a+b)

print('\n'.join(map(str, ans)))