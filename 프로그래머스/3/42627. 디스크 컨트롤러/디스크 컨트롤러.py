from heapq import heappush, heappop

def solution(jobs):
    jobs.sort()
    
    n = len(jobs)
    job_index = 0
    now = 0
    total = 0
    hq = []

    while job_index < n or hq:
        while job_index < n and jobs[job_index][0] <= now:
            start, time = jobs[job_index]
            heappush(hq, (time, start))
            job_index += 1
        
        if hq:
            time, start = heappop(hq)
            now += time
            total += now - start
        else:
            now = jobs[job_index][0]

    return total // n
