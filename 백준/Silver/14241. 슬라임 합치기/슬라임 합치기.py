from heapq import heapify, heappop, heappush

n = int(input())
sizes = list(map(int, input().split()))

heapify(sizes)

total = 0
while len(sizes) > 1:
    x, y = heappop(sizes), heappop(sizes)
    total += x * y
    heappush(sizes, x+y)

print(total)