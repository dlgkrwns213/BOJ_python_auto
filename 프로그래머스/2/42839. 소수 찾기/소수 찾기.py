from math import sqrt


def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if not n % i:
            return False
    return True


def backtracking(primes, numbers, idx, make):
    if is_prime(make):
        primes.add(make)
        
    if len(numbers) == idx:
        return
    
    backtracking(primes, numbers, idx+1, make*10)
    backtracking(primes, numbers, idx+1, make*10 + numbers[idx])
    

def solution(numbers):
    primes = set()
    backtracking(primes, list(map(int, numbers)), -1, 0)
    return len(primes)