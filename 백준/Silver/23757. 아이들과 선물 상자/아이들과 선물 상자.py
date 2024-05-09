from heapq import heappop, heappush, heapify

n, m = map(int, input().split())
presents = list(map(lambda present: -int(present), input().split()))
heapify(presents)

possible = True
for want in map(int, input().split()):
    present = -heappop(presents)
    if want > present:
        possible = False
        break

    heappush(presents, want-present)

print(+possible)