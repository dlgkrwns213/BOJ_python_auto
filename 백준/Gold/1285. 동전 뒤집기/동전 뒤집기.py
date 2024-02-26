# https://www.acmicpc.net/problem/1285
import sys
input = sys.stdin.readline


def backtracking(idx, cnt):
    global mn
    if mn == 0:
        return
    
    if idx == n:
        now = 0
        x = 1
        for _ in range(n):
            cnt = sum(map(lambda coin: 1 if coin & x else 0, coins))
            now += min(cnt, n-cnt)
            x <<= 1

        mn = min(now, mn)
        return

    backtracking(idx+1, cnt)

    coins[idx] ^= total
    backtracking(idx+1, cnt+1)
    coins[idx] ^= total


n = int(input())
coins = [int(''.join(map(lambda coin: '1' if coin == 'T' else '0', input().rstrip())), 2) for _ in range(n)]

mn = n * n
total = (1 << n) - 1
backtracking(0, 0)

print(mn)