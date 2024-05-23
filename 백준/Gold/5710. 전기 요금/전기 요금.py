# https://www.acmicpc.net/problem/5710
import sys
input = sys.stdin.readline


def get_cost(watt):
    total = 0
    if watt > 1000000:
        total += (watt - 1000000) * 7
        watt = 1000000
    if watt > 10000:
        total += (watt - 10000) * 5
        watt = 10000
    if watt > 100:
        total += (watt - 100) * 3
        watt = 100
    total += watt * 2
    return total


def get_watt(cost):
    total = 0
    if cost > 4979900:
        total += (cost - 4979900) // 7
        cost = 4979900
    if cost > 29900:
        total += (cost - 29900) // 5
        cost = 29900
    if cost > 200:
        total += (cost - 200) // 3
        cost = 200
    total += cost // 2
    return total


ans = []
while 1:
    a, b = map(int, input().split())
    if not a and not b:
        break

    total_watt = get_watt(a)

    left, right = 0, total_watt >> 1
    while left < right:
        mid = left + right >> 1
        neighbor_watt = total_watt - mid
        if get_cost(neighbor_watt) - get_cost(mid) > b:
            left = mid + 1
        else:
            right = mid
    ans.append(get_cost(left))
print('\n'.join(map(str, ans)))