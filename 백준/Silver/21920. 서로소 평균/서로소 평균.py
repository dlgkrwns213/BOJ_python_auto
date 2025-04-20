from math import gcd

n = int(input())
nums = list(map(int, input().split()))
x = int(input())
disjoints = [num for num in nums if gcd(num, x) == 1]

print(sum(disjoints) / len(disjoints))