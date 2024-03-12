# https://www.acmicpc.net/problem/2696
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    m = int(input())
    nums = sum((list(map(int, input().split())) for _ in range(m//10+1)), [])

    middles = [nums[0]]
    # 중간수, mid 보다 큰수 정렬, mid 보다 작은수 정렬
    mid, bigger, smaller = nums[0], [], []
    for i in range(m >> 1):
        a, b = nums[i << 1 | 1], nums[(i+1) << 1]
        if a > b:
            a, b = b, a

        # 새로 들어오는 숫자들과 비교해서 mid 값 구하기
        if mid < a:
            heappush(smaller, -mid)
            heappush(bigger, a)
            heappush(bigger, b)
            mid = heappop(bigger)
        elif mid > b:
            heappush(bigger, mid)
            heappush(smaller, -a)
            heappush(smaller, -b)
            mid = -heappop(smaller)
        else:
            heappush(bigger, b)
            heappush(smaller, -a)
        middles.append(mid)

    # 출력 값 저장
    x = (m+1) >> 1
    ans.append(x)
    for i in range(0, x, 10):
        ans.append(' '.join(map(str, middles[i:i+10])))

print('\n'.join(map(str, ans)))