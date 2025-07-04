from heapq import heappush, heappop

def solution(jobs):
    jobs.sort()
    
    n, idx = len(jobs), 0
    total, now = 0, 0
    hq = []
    
    while idx < n or hq:
        while idx < n:
            start, time = jobs[idx]
            if now< start:
                break
                
            heappush(hq, (time, start))
            idx += 1
            
        if hq:
            time, start = heappop(hq)
            now += time
            total += now - start
        else:
            now = jobs[idx][0]
            
    return total // n