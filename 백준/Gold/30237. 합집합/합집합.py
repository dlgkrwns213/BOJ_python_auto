# https://www.acmicpc.net/problem/30237
import sys
input = sys.stdin.readline


def list_to_bitmask(numbers):
    ret = 0
    for number in map(int, numbers):
        ret |= 1 << number - 1
    return ret


answers = []
for _ in range(int(input())):
    n = int(input())
    bitmasks = [list_to_bitmask(input().split()[1:]) for _ in range(n)]

    total = 0
    for bitmask in bitmasks:
        total |= bitmask

    ans = 0
    for i in range(50):
        if (1 << i) & total:
            now = 0
            for bitmask in bitmasks:
                if not (1 << i) & bitmask:
                    now |= bitmask


            ans = max(ans, bin(now).count('1'))

    answers.append(ans)

print('\n'.join(map(str, answers)))