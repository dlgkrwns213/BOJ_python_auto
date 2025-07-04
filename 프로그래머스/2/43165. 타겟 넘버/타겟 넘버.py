count = 0

def solution(numbers, target):
    backtracking(numbers, target, 0, 0)
    return count


def backtracking(numbers, target, idx, make):
    global count
    if idx == len(numbers):
        if target == make:
            count += 1
        return
    
    backtracking(numbers, target, idx+1, make+numbers[idx])
    backtracking(numbers, target, idx+1, make-numbers[idx])
    