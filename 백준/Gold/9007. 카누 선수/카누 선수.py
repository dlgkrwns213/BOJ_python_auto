# https://www.acmicpc.net/problem/9007
import sys
input = sys.stdin.readline


answers = []
for _ in range(int(input())):
    k, n = map(int, input().split())

    one = list(map(int, input().split()))
    two = list(map(int, input().split()))
    weight = sorted(a+b for a in one for b in two)

    # del one, two

    three = list(map(int, input().split()))
    four = list(map(int, input().split()))
    mn, ans = sys.maxsize, -1
    for w in (a+b for a in three for b in four):
        rest = k - w
        left, right = 0, n*n
        while left < right:
            mid = left + right >> 1
            now = weight[mid]
            if now > rest:
                right = mid
            elif now < rest:
                left = mid + 1
            else:
                mn = 0
                ans = k
                break

            gap = abs(rest - now)
            if mn > gap:
                mn = gap
                ans = w + now
            elif mn == gap:
                ans = min(ans, w + now)

        if mn == 0:
            break

    # del three, four, weight

    answers.append(ans)

print('\n'.join(map(str, answers)))