from heapq import heappop, heappush


def solution(jobs):
    hq = []
    start_time = [0] * len(jobs)
    for idx, job in enumerate(jobs):
        start, time = job
        start_time[idx] = start
        heappush(hq, (time, start, idx))
        
    total = 0
    now = 0
    while hq:
        time, start, idx = heappop(hq)
        
        now = max(now, start) + time
        total += now - start_time[idx]
        
    return total // len(jobs)
        
    