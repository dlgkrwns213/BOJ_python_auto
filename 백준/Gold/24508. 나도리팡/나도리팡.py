# https://www.acmicpc.net/problem/24508
def get_ans():
    if sum(nums) % k:
        return 0

    nums.sort()

    left, right = 0, n-1
    cnt = 0
    while left < right and cnt <= t:
        now = nums[left] + nums[right]
        if now < k:
            nums[right] += nums[left]
            cnt += nums[left]
            # nums[left] = 0
            left += 1
        else:
            nums[left] -= k - nums[right]
            cnt += k - nums[right]
            # nums[right] = k
            right -= 1

    return 1 if cnt <= t else 0


n, k, t = map(int, input().split())
nums = list(map(int, input().split()))

print('YES' if get_ans() else 'NO')