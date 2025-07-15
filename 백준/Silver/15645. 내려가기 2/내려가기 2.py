import sys
input = sys.stdin.readline


def get_score(func):
    now = nums[0]
    for i in range(1, n):
        nxt = [0] * 3
        nxt[0] = func(now[0], now[1]) + nums[i][0]
        nxt[1] = func(now[0], now[1], now[2]) + nums[i][1]
        nxt[2] = func(now[1], now[2]) + nums[i][2]
        now = nxt

    return func(now)


n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
print(get_score(max), get_score(min))