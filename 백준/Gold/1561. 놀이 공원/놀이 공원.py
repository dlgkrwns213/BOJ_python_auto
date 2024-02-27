# https://www.acmicpc.net/problem/1561
import sys
input = sys.stdin.readline


def get_child(now):
    return m + sum(map(lambda time: now // time, times))


n, m = map(int, input().split())
times = list(map(int, input().split()))

if n < m:
    print(n)
else:
    left, right = 0, 30*n
    while left < right:
        mid = left + right >> 1

        if get_child(mid) >= n:
            right = mid
        else:
            left = mid + 1

    rest = n - sum(map(lambda time: (left-1)//time + 1, times))
    for idx, time in enumerate(times):
        if left % time == 0:
            rest -= 1
            if rest == 0:
                print(idx+1)
                break