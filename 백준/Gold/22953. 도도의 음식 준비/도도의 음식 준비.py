# https://www.acmicpc.net/problem/22953
INF = float('inf')


def find_min_time():
    global mn_time
    left, right = 0, int(2e12)

    while left < right:
        mid = left + right >> 1
        make = sum(map(lambda time: mid // time, times))

        if make >= k:
            right = mid
        else:
            left = mid + 1

    mn_time = min(mn_time, left)


def backtracking(rest, idx=0):
    if idx == n:
        find_min_time()
        return

    for use in range(rest+1):
        if times[idx] - use < 1:
            break

        times[idx] -= use
        backtracking(rest-use, idx+1)
        times[idx] += use


n, k, c = map(int, input().split())
times = list(map(int, input().split()))

mn_time = INF
backtracking(c)
print(mn_time if mn_time != INF else sum(map(lambda time: k // time, times)))