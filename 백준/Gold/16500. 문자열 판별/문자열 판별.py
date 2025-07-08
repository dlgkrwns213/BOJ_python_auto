# https://www.acmicpc.net/problem/16500
import sys
input = sys.stdin.readline


want = input().rstrip()
n = int(input())
words = [input().rstrip() for _ in range(n)]

size = len(want)
dp = [0] * (size+1)
dp[0] = 1
for idx in range(1, size+1):
    for word in words:
        if len(word) <= idx and want[idx-len(word):idx] == word:
            dp[idx] |= dp[idx - len(word)]

print(dp[-1])