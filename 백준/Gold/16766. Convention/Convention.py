# https://www.acmicpc.net/problem/16766
def checking(time):
    start, cow_cnt, bus_cnt = waits[0], 0, 1
    for wait in waits:
        if cow_cnt == c or wait - start > time:
            bus_cnt += 1
            start = wait
            cow_cnt = 1
        else:
            cow_cnt += 1

        if bus_cnt > m:
            return False
    return True


n, m, c = map(int, input().split())
waits = sorted(map(int, input().split()))

left, right = 0, waits[-1]
while left < right:
    mid = left + right >> 1
    if checking(mid):
        right = mid
    else:
        left = mid + 1

print(left)