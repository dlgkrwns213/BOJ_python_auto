from math import sqrt

s = set()
def solution(numbers):
    backtracking(numbers, 0, "0")
    return len(s)
    
    
def backtracking(numbers, used, make):
    if is_prime(int(make)):
        s.add(int(make))
        
    for idx, val in enumerate(numbers):
        idx_bit = 1 << idx
        if not idx_bit & used:
            backtracking(numbers, used | idx_bit, make + val)
        
    
def is_prime(n):
    if n in (0, 1):
        return False
    
    for i in range(2, int(sqrt(n))+1):
        if not n%i:
            return False
    return True
    