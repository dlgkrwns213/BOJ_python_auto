def solution(wallet, bill):
    wallet.sort()
    bill.sort()
    
    answer = 0
    while wallet[0] < bill[0] or wallet[1] < bill[1]:
        bill[1] >>= 1
        bill = sorted(bill)
        answer += 1
    
    return answer