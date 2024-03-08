from heapq import heappush, heappop, heapify

def solution(scoville, K):
    hq = scoville.copy()
    heapify(hq)
    
    count = 0
    while len(hq) >= 2 and hq[0] < K:
        a = heappop(hq)
        b = heappop(hq)
        heappush(hq, a+2*b)
        count += 1
        
    return count if hq[0] >= K else -1
        

