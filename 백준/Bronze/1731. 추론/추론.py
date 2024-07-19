import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

a, b, c = nums[:3]
if a + c == 2 * b:
    print(nums[-1] + b - a)
else:
    print(nums[-1] // a * b)