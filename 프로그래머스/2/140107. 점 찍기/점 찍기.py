from math import sqrt

def solution(k, d):
    answer = d // k + 1
    
    for x in range(k, d+1, k):
        mx_y = int(sqrt(d*d - x*x))
        answer += mx_y // k + 1
    return answer