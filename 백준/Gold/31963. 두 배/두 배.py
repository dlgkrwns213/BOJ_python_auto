n = int(input())
nums = list(map(lambda x: bin(int(x))[2:], input().split()))

bef = '0'
count = 0
for num in nums:
    gap = len(bef) - len(num)
    if gap < 0 or (gap == 0 and num > bef):
        bef = num
    else:
        gap += 1 if num + '0'*gap < bef else 0
        bef = num + '0' * gap
        count += gap

print(count)