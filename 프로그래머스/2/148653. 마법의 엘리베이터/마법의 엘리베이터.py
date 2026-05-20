


def solution(storey):
    def recur(now, count):
        nonlocal mn
        
        if mn < count:
            return
        if now == 0:
            mn = min(mn, count)
            return
        
        last = now % 10
        recur((now-last)//10, count+last)
        recur((now+10-last)//10, count+(10-last))
        
    
    
    mn = int(1e9)
    recur(storey, 0)
    
    return mn

        