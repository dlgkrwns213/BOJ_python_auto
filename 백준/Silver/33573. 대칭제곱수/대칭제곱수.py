import sys
from math import sqrt
input = sys.stdin.readline


def is_square(s: str):
    num = int(s)
    return int(sqrt(num))**2 == num


ans = []
for _ in range(int(input())):
    ipt = input().rstrip()
    ans.append(is_square(ipt) and is_square(ipt[::-1]))

print('\n'.join(map(lambda x: "YES" if x else "NO", ans)))