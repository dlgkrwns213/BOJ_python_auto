nums = [0] * 256
for i in range(256):
    nums[i ^ (i << 1) & 255] = i

input()
print(' '.join(map(lambda x: str(nums[x]), map(int, input().split()))))