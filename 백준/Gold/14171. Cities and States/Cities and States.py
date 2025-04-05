# https://www.acmicpc.net/problem/14171
import sys
input = sys.stdin.readline


def change(code):
    x, y = map(lambda c: ord(c)-ord('A'), code)
    return x * 26 + y


counts = [0] * 676 * 676
for _ in range(int(input())):
    city, state_code = input().split()
    nc, mc = map(change, (city[:2], state_code))
    counts[nc * 676 + mc] += 1

count = 0
for i, v in enumerate(counts):
    x, y = divmod(i, 676)
    if x < y:
        count += v * counts[y*676+x]

print(count)