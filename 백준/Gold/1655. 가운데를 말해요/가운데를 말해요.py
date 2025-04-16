import heapq, sys
input = sys.stdin.readline

min_heap, max_heap = [], []
for i in range(int(input())):
    # max_heap에 먼저
    if i%2:
        heapq.heappush(min_heap, int(input()))
    else:
        heapq.heappush(max_heap, -int(input()))

    if min_heap and max_heap[0] < -min_heap[0]:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    print(-max_heap[0])