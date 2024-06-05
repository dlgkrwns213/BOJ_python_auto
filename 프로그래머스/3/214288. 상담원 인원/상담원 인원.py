from heapq import heappush, heappop
INF = int(1e9)
mn = INF

def solution(k, n, reqs):
    def works(advisers):
        wait = 0
        for cs_type, adviser in enumerate(advisers):
            hq = []
            for start, time in css[cs_type]:
                if len(hq) < adviser:
                    heappush(hq, start+time)
                else:
                    finish = heappop(hq)
                    if finish > start:
                        wait += finish - start
                        start = finish
                    heappush(hq, start + time)
        return wait
    
    
    def backtracking(idx, rest, advisers):
        global mn
        if idx == k-1:
            advisers.append(rest)
            mn = min(mn, works(advisers))
            advisers.pop()
            return
        
        for i in range(1, rest):
            advisers.append(i)
            backtracking(idx+1, rest-i, advisers)
            advisers.pop()
            
    
    css = [[] for _ in range(k)]
    for start, time, cs_type in reqs:
        css[cs_type-1].append((start, time))
    
    backtracking(0, n, [])
    return mn