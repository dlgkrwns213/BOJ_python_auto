def counting(find):
    total, idx = 0, 0
    for i, num in enumerate(nums):
        if num == find:
            total += i - idx
            idx += 1

    return total


n = int(input())
nums = list(map(lambda x: int(x[-1]) & 1, input().split()))

print(min(counting(0), counting(1)))