# https://www.acmicpc.net/problem/13710
def num2binary(num: int) -> str:
    bin_num = bin(num)[2:]
    return f'{"0" * (31 - len(bin_num))}{bin_num}'


def binary2num(binary: list) -> int:
    return sum((1 << 30-i) * int(v) for i, v in enumerate(binary))


n = int(input())
nums = list(map(int, input().split()))

bits, total = [0] * 31, nums[0]
for i, v in enumerate(num2binary(nums[0])):
    bits[i] = 1 if v == '1' else 0

for idx, num in enumerate(nums[1:]):
    bin_num = num2binary(num)
    for i, v in enumerate(bin_num):
        one, zero = bits[i], idx + 1 - bits[i]
        bits[i] = zero if v == '1' else one

    total += binary2num(bits) + num

    for i, v in enumerate(bin_num):
        bits[i] += 1 if v == '1' else 0

print(total)