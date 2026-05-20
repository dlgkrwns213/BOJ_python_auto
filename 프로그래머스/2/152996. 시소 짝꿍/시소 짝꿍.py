from collections import Counter

def solution(weights):
    counts = Counter(weights)
    
    total = 0
    for weight in counts:
        count = counts[weight]
        total += count * (count-1) // 2
    
    for weight in weights:
        for x in (2, 3, 4):
            for y in (2, 3, 4):
                pair = weight * x / y
                if pair <= weight:
                    continue
                total += counts.get(pair, 0)
                
    return total
    
    